import importlib.metadata
from typing import List, Union

import requests
import typer
from packaging.version import Version


def _normalize_value(value: Union[str, bool]) -> str:
    if isinstance(value, str):
        return value
    elif isinstance(value, bool):
        return 'true' if value else 'false'


def set_output(name: str, value: Union[str, bool]) -> None:
    """
    Sets GitHub action output.
    """
    print(f'::set-output name={name}::{_normalize_value(value)}')


def get_local_version(package_name: str) -> str:
    """
    Gets the local version.
    """
    return importlib.metadata.version(package_name)


def _get_pypi_versions(package_name: str, test_pypi: bool) -> List[str]:
    test = 'test.' if test_pypi else ''
    url = f'https://{test}pypi.org/pypi/{package_name}/json'
    r = requests.get(url)

    # Package don't exists (yet)
    if r.status_code == 404:
        return []

    versions = list(r.json()['releases'])
    versions.sort(key=Version)
    return versions


def get_pypi_version(package_name: str, test_pypi: bool = False) -> str:
    """
    Gets the latest PyPI version.
    """
    all_versions = _get_pypi_versions(package_name, test_pypi)
    if all_versions:
        return all_versions[-1]
    # No PyPI release yet
    else:
        return '0.0.0'


def main(package_name: str) -> None:
    """
    Main command

    Outputs:
    -------
    should-release: bool
        Whether local_version > pypi_version ("true" or "false")

    should-publish-test: bool
        Whether local_version > test_pypi_version ("true" or "false")
    """
    local_version = get_local_version(package_name)
    pypi_version = Version(get_pypi_version(package_name))
    test_pypi_version = Version(get_pypi_version(package_name, test_pypi=True))
    set_output('version', local_version)

    local_version = Version(local_version)
    set_output('should-publish', local_version > pypi_version)
    set_output('should-publish-test', local_version > test_pypi_version)


if __name__ == '__main__':
    typer.run(main)
