from pathlib import Path

from alskg.etl.validate_neo4j import Status, csv_data_rows, exit_code


def test_csv_data_rows_excludes_header(tmp_path: Path) -> None:
    csv_path = tmp_path / "example.csv"
    csv_path.write_text("col1,col2\n1,2\n3,4\n", encoding="utf-8")
    assert csv_data_rows(csv_path) == 2


def test_csv_data_rows_handles_header_only_file(tmp_path: Path) -> None:
    csv_path = tmp_path / "empty.csv"
    csv_path.write_text("col1,col2\n", encoding="utf-8")
    assert csv_data_rows(csv_path) == 0


def test_exit_code_prioritizes_failures() -> None:
    results = [
        type("R", (), {"status": Status.PASS}),
        type("R", (), {"status": Status.WARN}),
        type("R", (), {"status": Status.FAIL}),
    ]
    assert exit_code(results) == 1


def test_exit_code_can_fail_on_warnings() -> None:
    results = [type("R", (), {"status": Status.WARN})]
    assert exit_code(results, fail_on_warn=True) == 2
