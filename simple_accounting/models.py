from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Ledger(models.Model):
    LEDGER_TYPE_ASSETS = 0
    LEDGER_TYPE_CAPITAL = 1
    LEDGER_TYPE_LIABILITIES = 2
    LEDGER_TYPE_REVENUE = 3
    LEDGER_TYPE_EXPENSES = 4

    LEDGER_TYPES = [
        (LEDGER_TYPE_ASSETS, _("Assets")),
        (LEDGER_TYPE_CAPITAL, _("Capital")),
        (LEDGER_TYPE_LIABILITIES, _("Liabilities")),
        (LEDGER_TYPE_REVENUE, _("Revenue")),
        (LEDGER_TYPE_EXPENSES, _("Expenses"))
    ]

    ledger_type = models.IntegerField(choices=LEDGER_TYPES)

    name = models.CharField(
        help_text=_("Name of this ledger"),
        max_length=256
    )

    description = models.TextField(
        help_text=_("Any notes to go along with this Transaction."),
        blank=True
    )

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    TRANSACTION_MANUAL = 0
    TRANSACTION_AUTOMATED = 1

    TRANSACTION_TYPES = [
        (TRANSACTION_MANUAL, _("Manual")),
        (TRANSACTION_AUTOMATED, _("Automated")),
    ]

    transaction_type = models.IntegerField(choices=TRANSACTION_TYPES)

    notes = models.TextField(
        help_text=_("Any notes to go along with this Transaction."),
        blank=True
    )
    voids = models.OneToOneField(
        "Transaction",
        blank=True,
        null=True,
        related_name="voided_by",
        on_delete=models.deletion.CASCADE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.deletion.CASCADE
    )

    posted_timestamp = models.DateTimeField(
        help_text=_("Time the transaction was posted."),
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    @property
    def balanced(self):
        entries = self.entries.all()
        credits = sum([e.credit if e.credit else 0 for e in entries])
        debits = sum([e.debit if e.debit else 0 for e in entries])
        return credits == debits

    def __str__(self):
        return f"ID: {self.id}"


class TransactionEvidence(models.Model):
    OBJECT_TYPE_ORDER = 0

    OBJECT_TYPES = [
        (OBJECT_TYPE_ORDER, _("Order"))
    ]

    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        related_name="evidences"
    )
    object_type = models.IntegerField(choices=OBJECT_TYPES)
    object_id = models.IntegerField()

    def __str__(self):
        return f"Type: {self.object_type}, "\
            "Object ID: {self.object_id} to Transaction: {self.transaction}"


class LedgerEntry(models.Model):
    ledger = models.ForeignKey(
        Ledger,
        on_delete=models.CASCADE,
        related_name="entries"
    )
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        related_name="entries"
    )

    debit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )
    credit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Entry: DEBIT: {self.debit}"\
            "CREDIT: {self.credit} Ledger: {self.ledger}"
