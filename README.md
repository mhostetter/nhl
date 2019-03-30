# nhl

[![PyPI version](https://badge.fury.io/py/nhl.svg)](https://badge.fury.io/py/nhl)
[![Documentation Status](https://readthedocs.org/projects/nhl/badge/?version=latest)](https://nhl.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/mhostetter/nhl.svg?branch=master)](https://travis-ci.org/mhostetter/nhl)
[![Codecov](https://codecov.io/gh/mhostetter/nhl/branch/master/graph/badge.svg)](https://codecov.io/gh/mhostetter/nhl)

A python API for retrieving NHL game and player stats.

## Dependencies

```bash
   $ pip3 install --user dataclasses  # Not needed for python3.7 and greater
   $ pip3 install --user requests
   $ pip3 install --user beautifulsoup4
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
