# PyPI Publisher
GitHub action to build and publish
[PEP 518](https://peps.python.org/pep-0518/) compliant projects (Setuptools,
Flit, Poetry) on PyPI when local version is higher than PyPI's.

## Usage
```yaml
name: Publish
on:
  workflow_dispatch:
    branches:
      - main

jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    steps:
      - use: alirezatheh/pypi-publisher@v1
        with:
          test-api-pypi-token: ${{ secrets.TEST_PYPI_API_TOKEN }}
          pypi-api-token: ${{ secrets.PYPI_API_TOKEN }}
```

The action assume:
- The project has a `pyproject.toml` or `setup.py` in the top-level directory.
- Python and pip are installed (e.g. by `actions/setup-python@v2`).

## Inputs
- `test-api-pypi-token`: API token of the Test PyPI account publishing the
  project. If missing, publish on Test PyPI is skipped. (optional)
- `pypi-api-token`: API token of the PyPI account publishing the project.
  (required)

## Acknowledgements
This action is inspired by
[pypi-auto-publish](https://github.com/etils-actions/pypi-auto-publish)
