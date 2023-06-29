from pydantic import BaseModel


class Signs(BaseModel):
    debit: int
    credit: int


def signs(ledger_type: int) -> Signs:
    if ledger_type == 0:  # ASSETS
        return Signs(debit=1, credit=-1)
    elif ledger_type == 1:  # CAPITAL
        return Signs(debit=-1, credit=1)
    elif ledger_type == 2:  # LIABILITIES
        return Signs(debit=-1, credit=1)
    elif ledger_type == 3:  # REVENUE
        return Signs(debit=-1, credit=1)
    elif ledger_type == 4:  # EXPENSES
        return Signs(debit=1, credit=-1)
    else:
        raise RuntimeError(f"Unhandled ledger_type: {ledger_type}")
