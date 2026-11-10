"""Інтерактивне меню менеджера особистих фінансів."""

import math

from financial_statistics import (
    calculate_balance,
    calculate_expenses,
    calculate_income,
)
from transactions import (
    add_transaction,
    delete_transaction,
    filter_by_category,
    show_transactions,
)


def read_amount() -> float | None:
    """Запитує додатну скінченну суму; повертає None при некоректному вводі."""
    try:
        amount = float(input("Сума: ").strip())
    except ValueError:
        print("Введіть коректне число.")
        return None

    if not math.isfinite(amount) or amount <= 0:
        print("Сума має бути додатним скінченним числом.")
        return None
    return amount


def add_from_menu(transactions: list[dict], transaction_type: str) -> None:
    amount = read_amount()
    if amount is None:
        return

    category = input("Категорія: ").strip()
    description = input("Опис: ").strip()
    if not category or not description:
        print("Категорія й опис не мають бути порожніми.")
        return

    add_transaction(transactions, transaction_type, amount, category, description)


def print_summary(label: str, amount: object) -> None:
    print(f"{label}: {amount:.2f}")


def main() -> None:
    transactions: list[dict] = []
    actions = {
        "1": ("Додати дохід", lambda: add_from_menu(transactions, "income")),
        "2": ("Додати витрату", lambda: add_from_menu(transactions, "expense")),
        "3": ("Показати транзакції", lambda: show_transactions(transactions)),
        "4": ("Показати доходи", lambda: print_summary("Доходи", calculate_income(transactions))),
        "5": ("Показати витрати", lambda: print_summary("Витрати", calculate_expenses(transactions))),
        "6": ("Показати баланс", lambda: print_summary("Баланс", calculate_balance(transactions))),
        "7": ("Фільтрувати за категорією", lambda: show_filtered(transactions)),
        "8": ("Видалити транзакцію за ID", lambda: delete_from_menu(transactions)),
    }

    while True:
        print("\nМенеджер особистих фінансів")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Вийти")

        choice = input("Оберіть дію (0–8): ").strip()
        if choice == "0":
            print("До побачення!")
            break
        action = actions.get(choice)
        if action is None:
            print("Невідома дія. Оберіть число від 0 до 8.")
            continue
        action[1]()


def show_filtered(transactions: list[dict]) -> None:
    category = input("Категорія для пошуку: ").strip()
    matches = filter_by_category(transactions, category)
    if matches:
        show_transactions(matches)
    else:
        print("Транзакцій у цій категорії не знайдено.")


def delete_from_menu(transactions: list[dict]) -> None:
    try:
        transaction_id = int(input("ID транзакції: ").strip())
    except ValueError:
        print("ID має бути цілим числом.")
        return
    _, message = delete_transaction(transactions, transaction_id)
    print(message)


if __name__ == "__main__":
    main()
