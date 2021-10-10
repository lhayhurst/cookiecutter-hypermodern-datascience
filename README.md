# modern-python-datascience-cookiecutter

This [cookiecutter](https://cookiecutter.readthedocs.io/) project is a [Make](https://www.gnu.org/software/make/)-friendly, Github Actions
CI/CD [batteries included](.github/workflows/python-app.yml) starter Python project that
combines [Poetry](https://python-poetry.org/docs/) and [Nox](https://nox.thea.codes/en/stable/). It is partially
inspired by Claudio Jolowicz's [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
article series.

At present, it includes numpy, pandas and jupyterlab for data science packages.

Run:

```shell
 cookiecutter https://github.com/lhayhurst/modern-python-datascience-cookiecutter.git
 ```

To use it. Once you've run cookiecutter, do:

```shell
make deps  # to build python and run the tests
make jupyterlab  # to run jupyterlab
make lint # to lint your code
make  # to see what else you can do

```
