<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# ALS-KG

ALS-KG is a LinkML-based schema and ontology project for representing knowledge relevant to amyotrophic lateral sclerosis (ALS), including diseases, phenotypes, genes, proteins, variants, drugs, exposures, and their associations.

## Repository

[https://github.com/cair2015/als-kg](https://github.com/cair2015/als-kg)

## Documentation Website

[https://cair2015.github.io/als-kg](https://cair2015.github.io/als-kg)

## Development Workflow

The schema source of truth is:

`src/alskg/schema/als_kg.yaml`

Common commands:

```bash
just gen-doc
just gen-project
just test
NEO4J_PASSWORD='<password>' uv run als-kg-validate-neo4j
```

These commands regenerate documentation, rebuild generated artifacts, and validate the project.

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
  * [schema/](docs/schema/) - published schema artifacts
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [alskg](src/alskg)
    * [schema/](src/alskg/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/alskg/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
