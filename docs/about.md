# About ALS-KG

`als_kg` is a LinkML-based schema project for describing the ALS Knowledge Graph in an ontology-friendly form.

The repository is organized around a single primary source schema:

`src/als_kg/schema/als_kg.yaml`

From that schema, the project generates:

- LinkML reference documentation under `docs/elements/`
- published schema artifacts under `docs/schema/`
- Python dataclasses and Pydantic models under `src/als_kg/datamodel/`

## Documentation Workflow

Common commands:

```bash
just gen-doc
just gen-project
just test
```

`just gen-doc` recreates the static MkDocs pages from `src/docs/` and regenerates the LinkML reference pages, so the documentation site can be rebuilt even if `docs/` was removed.
