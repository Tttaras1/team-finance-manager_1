from decimal import Decimal


def calculate_income(transactions: list[dict]) -> Decimal:
    """Повертає загальну суму доходів."""
    return sum(
        (Decimal(str(t["amount"])) for t in transactions if t["type"] == "income"),
        Decimal("0"),
    )


def calculate_expenses(transactions: list[dict]) -> Decimal:
    """Повертає загальну суму витрат."""
    return sum(
        (Decimal(str(t["amount"])) for t in transactions if t["type"] == "expense"),
        Decimal("0"),
    )


def calculate_balance(transactions: list[dict]) -> Decimal:
    """Повертає різницю між доходами та витратами."""
    return calculate_income(transactions) - calculate_expenses(transactions)
