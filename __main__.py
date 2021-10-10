"""Command-line interface."""
import os
import sys

import typer

from foo import __version__ as main_version

app = typer.Typer()


@app.command()
def version() -> None:
    typer.echo(main_version)
    return


@app.command()
def about() -> None:
    ppath = os.environ["PYTHONPATH"]
    typer.echo(f"python = {sys.executable}\nPYTHONPATH = {ppath}\nprogram  = {__name__}\nprogram args = {sys.argv}")
    return


if __name__ == "__main__":
    app()
