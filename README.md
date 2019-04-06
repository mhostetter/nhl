# nhl

[![PyPI version](https://badge.fury.io/py/nhl.svg)](https://badge.fury.io/py/nhl)
[![Documentation Status](https://readthedocs.org/projects/nhl/badge/?version=latest)](https://nhl.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/mhostetter/nhl.svg?branch=master)](https://travis-ci.org/mhostetter/nhl)
[![Codecov](https://codecov.io/gh/mhostetter/nhl/branch/master/graph/badge.svg)](https://codecov.io/gh/mhostetter/nhl)

A python API for retrieving NHL game and player stats.

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
