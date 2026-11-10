def add_transaction(transactions, transaction_type, amount, category, description):
    if not isinstance (amount, ( int , float)) or amount <= 0:
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


def show_transactions(transactions):
   if not transactions:
       print("Список порожній")
       return
   
   print(f"{'ID' :<3} | {'TYPE' :<7} | {'AMOUNT' :<9} | {'CATEGORY' :<11} | {'DESCRIPTION' :<13}"  )
   print("-" * 50)
   for i in transactions :
        print(f"{i['id']:<3} | {i['type']:<7} | {i['amount']:<9} | {i['category']:<11} | {i['description']:<13}")