import pytest

from datetime import datetime
from django.contrib.auth.models import User

from simple_accounting.models import Ledger, LedgerEntry, Transaction


@pytest.mark.django_db
def test_balanced_transaction():
	admin = User.objects.get(email="admin@localhost")
	t = Transaction.objects.create(transaction_type=Transaction.TRANSACTION_AUTOMATED, posted_timestamp=datetime.now(), owner=admin)

	cash_ledger = Ledger.objects.get(name="Cash")
	investments_ledger = Ledger.objects.get(name="Investments")

	LedgerEntry.objects.create(transaction=t, ledger=cash_ledger, debit=5000)
	LedgerEntry.objects.create(transaction=t, ledger=investments_ledger, credit=5000)

	assert t.balanced


@pytest.mark.django_db
def test_unbalanced_transaction():
	admin = User.objects.get(email="admin@localhost")
	t = Transaction.objects.create(transaction_type=Transaction.TRANSACTION_AUTOMATED, posted_timestamp=datetime.now(), owner=admin)

	cash_ledger = Ledger.objects.get(name="Cash")
	investments_ledger = Ledger.objects.get(name="Investments")

	LedgerEntry.objects.create(transaction=t, ledger=cash_ledger, debit=5000)
	LedgerEntry.objects.create(transaction=t, ledger=investments_ledger, credit=5001)

	assert not t.balanced