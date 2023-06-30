import pytest

from django.contrib.auth.models import User

from simple_accounting.models import Ledger



@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        User.objects.create(username="admin", email="admin@localhost")
        Ledger.objects.create(name="Cash", ledger_type=Ledger.LEDGER_TYPE_ASSETS)
        Ledger.objects.create(name="Accounts Receivable", ledger_type=Ledger.LEDGER_TYPE_ASSETS)
        Ledger.objects.create(name="Investments", ledger_type=Ledger.LEDGER_TYPE_CAPITAL)
        Ledger.objects.create(name="Accounts Payable", ledger_type=Ledger.LEDGER_TYPE_LIABILITIES)
        Ledger.objects.create(name="Sales", ledger_type=Ledger.LEDGER_TYPE_REVENUE)
