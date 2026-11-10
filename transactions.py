def add_transaction(transactions : list, transaction_type: str, amount: float, category: str, description: str) -> None:
    """Додає нову транзакцію до списку.

    Args:
        transactions (list): Список усіх транзакцій.
        transaction_type (str): Тип транзакції.
        amount (float): Сума транзакції.
        category (str): Категорія витрат чи доходів.
        description (str): Опис операції.

    Returns:
        None
    """
    if transaction_type not in ("income", "expense") :
        print("Транзакція повинна бути income або expense")
        return 
    if amount is None :
        return
    if not isinstance (amount, ( int , float)) or amount < 0:
        print("Cума має бути додатнім числом")
        return

    if not category:
        print("Категорія не має бути порожньою")
        return

    if not description :
        print("Опис не має бути порожнім")
        return

    new_id = transactions[-1]["id"] + 1 if transactions else 1
    transaction = {
    "id": new_id,
    "type": transaction_type,
    "amount": float(amount),
    "category": category,
    "description": description
    }
    transactions.append(transaction)
    print("Транзакцію додано")


def show_transactions(transactions: list) -> None:
   """Виводить список усіх транзакцій у вигляді таблиці.

    Args:
        transactions (list): Список транзакцій для відображення.

    Returns:
        None
    """
   if not transactions:
       print("Список порожній")
       return
   
   print(f"{'ID' :<3} | {'TYPE' :<7} | {'AMOUNT' :<9} | {'CATEGORY' :<11} | {'DESCRIPTION' :<13}"  )
   print("-" * 50)
   for transaction in transactions :
        print(f"{transaction['id']:<3} | {transaction['type']:<7} | {transaction['amount']:<9} | {transaction['category']:<11} | {transaction['description']:<13}")

def filter_by_category(transactions, category):
    """
    фільтрує та виводить транзакцію за категорією

    аргументи:
        transactions (list) - список поточних транзакцій
        category (str) - назва категорії для фільтрації

    повертає:
        список відфільтрованих транзакцій
    """
    category_lower = category.strip().casefold()
    return [
        transaction
        for transaction in transactions
        if transaction["category"].strip().casefold() == category_lower
    ]

def delete_transaction(transactions, transaction_id):
    """
    видаляє транзакцію за унікальним індексом або ID

    агрументи:
        transactions (list) - список поточних транзакцій
        transaction_id (int)- індекс транзакції для видалення

    повертає:
        оновлений список транзакцій та повідомлення про статус
    """
    for index, transaction in enumerate(transactions):
        if transaction["id"] == transaction_id:
            removed = transactions.pop(index)
            return transactions, f"видалено транзакцію {removed}"
    return transactions, "помилка. транзакцію не знайдено"