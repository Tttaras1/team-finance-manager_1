from decimal import Decimal


def calculate_income(transactions):
    return sum(
        (Decimal(str(t["amount"])) for t in transactions if t["type"] == "income"),
        Decimal("0"),
    )


def calculate_expenses(transactions):
    return sum(
        (Decimal(str(t["amount"])) for t in transactions if t["type"] == "expense"),
        Decimal("0"),
    )


def calculate_balance(transactions):
    return calculate_income(transactions) - calculate_expenses(transactions)
