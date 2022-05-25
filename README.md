# PyPI Publish
GitHub action to automate build and publish
[PEP 518](https://peps.python.org/pep-0518/) compliant projects (Setuptools,
Flit, Poetry) on Test PyPI and/or PyPI if local `package.__version__` is ahead
of PyPI's.

## Usage
```yaml
name: Publish
on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    steps:
      - use: alirezatheh/pypi-publish@v1
        with:
          test-api-pypi-token: ${{ secrets.TEST_PYPI_API_TOKEN }}
          pypi-api-token: ${{ secrets.PYPI_API_TOKEN }}
```

The action assume:
- The project has a `setup.py`, `setup.cfg` or `pyproject.toml` in the
  top-level directory.
- Python and pip are installed (e.g. by `actions/setup-python@v3`).

## Inputs
- `test-api-pypi-token`: API token of the Test PyPI account publishing the
  project. If missing, publish on Test PyPI is skipped. (optional)
- `pypi-api-token`: API token of the PyPI account publishing the project.
  (required)
- `package-name`: Name of the PyPI package, Defaults to repository name
  (optional).


## Acknowledgements
This action is inspired by
[pypi-auto-publish](https://github.com/etils-actions/pypi-auto-publish)
