# About ALS-KG

`alskg` is a LinkML-based schema project for describing the ALS Knowledge Graph in an ontology-friendly form.

The repository is organized around a single primary source schema:

`src/alskg/schema/alskg_schema.yaml`

From that schema, the project generates:

- OWL ontology under `project/owl/`
- SHACL shapes under `project/shacl/`
- Python dataclasses and Pydantic models under `src/alskg/datamodel/`
- LinkML reference documentation under `docs/elements/`

## Common commands

```bash
just gen-all     # generate OWL, SHACL, and Python models
just gen-doc     # regenerate schema reference docs
just serve       # preview docs locally
just test        # validate schema + run tests
just lint        # validate schema only
```
