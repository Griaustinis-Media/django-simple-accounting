from django.contrib import admin

from accounting.models import *


class LedgerAdmin(admin.ModelAdmin):
    list_display = ("name", "ledger_type")


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_type", "voids", "owner", "balanced", "posted_timestamp", "notes")


class LedgerEntryAdmin(admin.ModelAdmin):
    list_display = ("ledger", "transaction", "debit", "credit", "created_at")


admin.site.register(Ledger, LedgerAdmin)
admin.site.register(LedgerEntry, LedgerEntryAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionEvidence)
