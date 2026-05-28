from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

import polars as pl

DELIMITER = ";"
ARRAY_DELIMITER = "|"
CSV_QUOTING = csv.QUOTE_ALL  # Quote all fields to handle multiline content in Neo4j bulk import


def _sanitize_column_name(name: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9_]", "_", name)
    sanitized = re.sub(r"_+", "_", sanitized).strip("_")
    return sanitized or "property"


def _coerce_scalar(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (bool, int, float, str)):
        return value
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _flatten_properties(
    properties: dict[str, Any],
    *,
    prefix: str = "",
) -> dict[str, Any]:
    """Flatten nested property payloads into Neo4j-friendly columns.

    Neo4j bulk import does not support nested maps, so nested dicts become
    ``foo__bar`` columns. Lists of dicts are preserved as JSON-encoded strings
    within a string array, while lists of scalars remain arrays.
    """
    flat: dict[str, Any] = {}

    for raw_key, value in properties.items():
        key = _sanitize_column_name(raw_key)
        column = f"{prefix}__{key}" if prefix else key

        if isinstance(value, dict):
            flat.update(_flatten_properties(value, prefix=column))
        elif isinstance(value, list):
            if not value:
                flat[column] = []
            elif all(isinstance(item, dict) for item in value):
                flat[column] = [
                    json.dumps(item, sort_keys=True, separators=(",", ":"))
                    for item in value
                ]
            else:
                flat[column] = [_coerce_scalar(item) for item in value]
        else:
            flat[column] = _coerce_scalar(value)

    return flat


def _parse_properties(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    parsed = json.loads(raw)
    if parsed is None:
        return {}
    if not isinstance(parsed, dict):
        return {"properties_json": json.dumps(parsed, separators=(",", ":"))}
    return _flatten_properties(parsed)


def _infer_column_type(values: list[Any]) -> str:
    """Infer Neo4j bulk import column type from values.
    
    Returns Neo4j's native 64-bit types (long, double) to avoid 
    type normalization warnings during import.
    """
    non_null = [value for value in values if value is not None]
    if not non_null:
        return "string"

    if all(isinstance(value, list) for value in non_null):
        scalar_values = [item for value in non_null for item in value if item is not None]
        if scalar_values and all(isinstance(item, bool) for item in scalar_values):
            return "boolean[]"
        if scalar_values and all(
            isinstance(item, int) and not isinstance(item, bool) for item in scalar_values
        ):
            return "long[]"
        if scalar_values and all(
            isinstance(item, (int, float)) and not isinstance(item, bool)
            for item in scalar_values
        ):
            return "double[]"
        return "string[]"

    if all(isinstance(value, bool) for value in non_null):
        return "boolean"
    if all(isinstance(value, int) and not isinstance(value, bool) for value in non_null):
        return "long"
    if all(
        isinstance(value, (int, float)) and not isinstance(value, bool)
        for value in non_null
    ):
        return "double"
    return "string"


def _stringify_for_csv(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ARRAY_DELIMITER.join("" if item is None else str(item) for item in value)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _write_grouped_nodes(nodes: pl.DataFrame, out_dir: Path) -> list[Path]:
    """Write nodes grouped by label to separate CSV files.
    
    Args:
        nodes: DataFrame with required columns: id, label, properties
        out_dir: Output directory for CSV files
    
    Returns:
        List of written file paths
    
    Raises:
        ValueError: If required columns are missing
    """
    required_cols = {"id", "label", "properties"}
    missing = required_cols - set(nodes.columns)
    if missing:
        raise ValueError(f"Missing required columns in nodes: {missing}")
    
    nodes_dir = out_dir / "nodes"
    nodes_dir.mkdir(parents=True, exist_ok=True)
    
    files: list[Path] = []
    labels = nodes["label"].unique().drop_nulls().to_list()
    if not labels:
        return files

    for label in sorted(labels):
        df = nodes.filter(pl.col("label") == label)
        rows: list[dict[str, Any]] = []
        for row in df.iter_rows(named=True):
            props = _parse_properties(row.get("properties"))
            rows.append({"id": row["id"], "label": row["label"], **props})

        prop_names = sorted(
            {key for row in rows for key in row.keys() if key not in {"id", "label"}}
        )
        prop_types = {
            key: _infer_column_type([row.get(key) for row in rows]) for key in prop_names
        }

        output = nodes_dir / f"nodes_{label.lower()}.csv"
        with output.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=DELIMITER, quoting=CSV_QUOTING)
            header = ["id:ID"] + [f"{key}:{prop_types[key]}" for key in prop_names] + [":LABEL"]
            writer.writerow(header)
            for row in rows:
                writer.writerow(
                    [row["id"]]
                    + [_stringify_for_csv(row.get(key)) for key in prop_names]
                    + [row["label"]]
                )
        files.append(output)

    return files


def _write_grouped_edges(edges: pl.DataFrame, out_dir: Path) -> list[Path]:
    """Write edges grouped by label to separate CSV files.
    
    Args:
        edges: DataFrame with required columns: from, to, label, relation, undirected, properties
        out_dir: Output directory for CSV files
    
    Returns:
        List of written file paths
    
    Raises:
        ValueError: If required columns are missing
    """
    required_cols = {"from", "to", "label", "relation", "undirected", "properties"}
    missing = required_cols - set(edges.columns)
    if missing:
        raise ValueError(f"Missing required columns in edges: {missing}")
    
    edges_dir = out_dir / "edges"
    edges_dir.mkdir(parents=True, exist_ok=True)
    
    files: list[Path] = []
    labels = edges["label"].unique().drop_nulls().to_list()
    if not labels:
        return files

    for label in sorted(labels):
        df = edges.filter(pl.col("label") == label)
        rows: list[dict[str, Any]] = []
        for row in df.iter_rows(named=True):
            props = _parse_properties(row.get("properties"))
            rows.append(
                {
                    "from": row["from"],
                    "to": row["to"],
                    "type": row["relation"],
                    "kg_label": row["label"],
                    "undirected": row["undirected"],
                    **props,
                }
            )

        prop_names = sorted(
            {
                key
                for row in rows
                for key in row.keys()
                if key not in {"from", "to", "type"}
            }
        )
        prop_types = {
            key: _infer_column_type([row.get(key) for row in rows]) for key in prop_names
        }

        output = edges_dir / f"edges_{label.lower().replace('-', '_')}.csv"
        with output.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=DELIMITER, quoting=CSV_QUOTING)
            header = (
                [":START_ID"]
                + [f"{key}:{prop_types[key]}" for key in prop_names]
                + [":END_ID", ":TYPE"]
            )
            writer.writerow(header)
            for row in rows:
                writer.writerow(
                    [row["from"]]
                    + [_stringify_for_csv(row.get(key)) for key in prop_names]
                    + [row["to"], row["type"]]
                )
        files.append(output)

    return files


def _write_import_command(
    out_dir: Path,
    *,
    db_name: str,
    node_files: list[Path],
    edge_files: list[Path],
) -> None:
    # Convert absolute paths to relative paths from out_dir for portability
    node_args = " \\\n  ".join(
        f'--nodes="{path.relative_to(out_dir.parent)}"' for path in sorted(node_files)
    )
    edge_args = " \\\n  ".join(
        f'--relationships="{path.relative_to(out_dir.parent)}"' for path in sorted(edge_files)
    )

    command = f"""#!/usr/bin/env bash
set -euo pipefail

# Stop your Neo4j database before running this command.
neo4j-admin database import full {db_name} \\
  --overwrite-destination=true \\
  --delimiter="{DELIMITER}" \\
  --array-delimiter="{ARRAY_DELIMITER}" \\
  --multiline-fields=true \\
  --quote='"' \\
  {node_args} \\
  {edge_args}
"""
    script_path = out_dir / "neo4j-admin-import.sh"
    script_path.write_text(command, encoding="utf-8")
    script_path.chmod(0o755)


def _write_manifest(
    out_dir: Path,
    *,
    node_files: list[Path],
    edge_files: list[Path],
) -> None:
    manifest = {
        "delimiter": DELIMITER,
        "array_delimiter": ARRAY_DELIMITER,
        "node_files": [str(path.relative_to(out_dir.parent)) for path in sorted(node_files)],
        "edge_files": [str(path.relative_to(out_dir.parent)) for path in sorted(edge_files)],
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert OptimusKG Parquet exports into Neo4j bulk-import CSV files."
    )
    parser.add_argument("--nodes", type=Path, required=True, help="Path to nodes.parquet")
    parser.add_argument("--edges", type=Path, required=True, help="Path to edges.parquet")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("neo4j-import"),
        help="Directory to write Neo4j CSV files into.",
    )
    parser.add_argument(
        "--db-name",
        default="neo4j",
        help="Database name to use in the generated neo4j-admin import command.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Reading nodes from {args.nodes}...")
    nodes = pl.read_parquet(args.nodes)
    print(f"  Loaded {len(nodes):,} nodes")
    
    print(f"Reading edges from {args.edges}...")
    edges = pl.read_parquet(args.edges)
    print(f"  Loaded {len(edges):,} edges")

    node_files = _write_grouped_nodes(nodes, args.out_dir)
    edge_files = _write_grouped_edges(edges, args.out_dir)
    _write_import_command(
        args.out_dir,
        db_name=args.db_name,
        node_files=node_files,
        edge_files=edge_files,
    )
    _write_manifest(args.out_dir, node_files=node_files, edge_files=edge_files)

    print(f"Wrote {len(node_files)} node CSV files and {len(edge_files)} edge CSV files.")
    print(f"Import helper script: {args.out_dir / 'neo4j-admin-import.sh'}")


if __name__ == "__main__":
    main()


"""
uv run python scripts/optimuskg_parquet_to_neo4j_csv.py \
  --nodes data/optimuskg/nodes.parquet \
  --edges data/optimuskg/edges.parquet \
  --out-dir data/optimuskg/neo4j-import \
  --db-name neo4j
"""
