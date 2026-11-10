def calculate_income(transactions):
    return sum(t["amount"] for t in transactions if t["type"] == "income")


def calculate_expenses(transactions):
    return sum(t["amount"] for t in transactions if t["type"] == "expense")


def calculate_balance(transactions):
    return calculate_income(transactions) - calculate_expenses(transactions)
