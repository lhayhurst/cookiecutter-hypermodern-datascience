"""Test cases for the __main__ module."""
import sys

from typer.testing import CliRunner

from {{cookiecutter.package_name}} import __version__
from {{cookiecutter.package_name}}.__main__ import app

runner = CliRunner()


def test_get_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_about():
    result = runner.invoke(app, ["about"])
    assert result.exit_code == 0
    assert sys.executable in result.stdout
    print(result.stdout)
