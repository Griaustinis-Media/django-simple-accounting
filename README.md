# django-simple-accounting
Plain and Simple Accounting module for Django

[![PyPI version fury.io](https://badge.fury.io/py/django-simple-accounting.svg)](https://pypi.python.org/pypi/django-simple-accounting/)
[![PyPI download month](https://img.shields.io/pypi/dm/django-simple-accounting.svg)](https://pypi.python.org/pypi/django-simple-accounting/)
[![GitHub license](https://img.shields.io/github/license/Griaustinis-Media/django-simple-accounting.svg)](https://github.com/Griaustinis-Media/django-simple-accounting/blob/master/LICENSE)

## Installation

Install from pypi:

`pip install django-simple-accounting`

Add "simple_accounting" to your INSTALLED_APPS setting.

```
INSTALLED_APPS = [
    ...
    "simple_accounting",
]
```

## Usage
It is based on idea of [Double-Entry Bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping). This means, every transaction should consists of minimum one Debit and one Credit Entry.
Look at [examples](https://github.com/Griaustinis-Media/django-simple-accounting/blob/main/tests/test_transactions.py) as tests.

`transaction.balanced` is a basic validation if Credit and Debit sides are equal in this transaction. If not balanced - something's wrong inside data.
