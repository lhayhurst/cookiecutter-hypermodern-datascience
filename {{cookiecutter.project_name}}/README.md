![Build Status](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.github_project_name}}/actions/workflows/python-app.yml/badge.svg)

# {{cookiecutter.project_name}}
{{cookiecutter.description}}

## Getting Started

1. Install python3. The [first article]((https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)) in the series linked above should get you started (he recommends `pyenv`). For example, if using `pyenv`, run "pyenv local 3.9.2" (if using python v 3.9.2).
2. Install `poetry`; see the project homepage or [this article](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
3. Build the project. If you prefer make, you can run:

```bash
make deps
```

This will run `poetry install` and `poetry run nox --install-only`. You can run `make help` to see more make targets. Alternatively, you can just run `poetry`'s CLI; see [the Makefile](Makefile)'s make targets for inspiration. 

```bash
make clean
```

Will clean out your install. 

## Other make targets
Run `make` to get them: 

```shell
make     
black                          reformat all files for black. good for when someone else needs to read your code.
clean                          clean up project
cov                            run test coverage report
help                           me
lint                           run flake8 linter
safety                         check for open source vulnerabilities with safety
test                           run tests after running black check, flake8, and mypy
thorough                       the full treatment: black check, flake8, mypy, and safety
```

## Configuration

This file has some standard config files:

* The overall project is configured via a [PEP518](https://www.python.org/dev/peps/pep-0518/) [pyproject.toml](pyproject.toml) file. If you fork this repo, you should probably change it. It contains the [black](https://pypi.org/project/black/) settings, the project dependencies, a [pytest](https://docs.pytest.org/en/stable/index.html) configuration, and a 
* the [.gitignore](.gitignore) contains obvious gitignores. 
* the [noxfile.py](noxfile.py) contains nox targets for running `safety` and your `tests`. It uses the [nox-poetry](https://pypi.org/project/nox-poetry/) project for nox-poetry integration.
* The [.flake8](.flake8) has a minimal [flake8](https://flake8.pycqa.org/en/latest/) configuration.
* The [mypy.ini](mypy.ini) has a minimal [mypy](http://mypy-lang.org/) configuration.

## Adding a new python dependency

By way of example, you want to add scipy. Then you simply run:

```bash
poetry add scipy
```

## Running main
Run ```sh
 PYTHONPATH=src poetry run python -m {{cookiecutter.project_name}} --help
Usage: python -m {{cookiecutter.project_name}} [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  about
  version

```