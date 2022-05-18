# nhl

[![PyPI version](https://badge.fury.io/py/nhl.svg)](https://badge.fury.io/py/nhl)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/nhl)](https://pypistats.org/packages/nhl)
[![Read the Docs](https://img.shields.io/readthedocs/nhl)](https://nhl.readthedocs.io/en/latest/)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/mhostetter/nhl/Test)](https://github.com/mhostetter/nhl/actions)
[![Codecov](https://img.shields.io/codecov/c/github/mhostetter/nhl)](https://codecov.io/gh/mhostetter/nhl)
[![Twitter](https://img.shields.io/twitter/follow/nhl_py?label=nhl_py&style=flat&logo=twitter)](https://twitter.com/nhl_py)

A Python 3 API for NHL game and player stats

## Install

Install the latest released version via `pip`.

```bash
$ pip3 install nhl
```

Or you can install the latest pushed code via `git`.

```bash
$ git clone https://github.com/mhostetter/nhl
$ pip3 install -e nhl/
```

## Unit Testing

Required dependencies:

```bash
$ pip3 install --user pytest
$ pip3 install --user pytest-cov
$ pip3 install --user requests-mock
```

Run tests:

```bash
$ pytest .
```
