<<<<<<< HEAD
# Cash tracker
=======
# Budget Tracker
>>>>>>> main

Навчальна Python-програма для обліку доходів і витрат. Транзакції зберігаються в пам’яті лише під час роботи програми; збереження у файл або базу даних поки не реалізоване.

## Можливості

- Додавання доходів і витрат із сумою, категорією та описом.
- Перегляд усіх транзакцій у таблиці.
- Видалення транзакції за її ID.
- Підрахунок доходів, витрат і поточного балансу.
- Фільтрація транзакцій за категорією без урахування регістру.
- Обробка некоректного числового введення в меню.

Для суми дозволені лише додатні скінченні числа. Тип транзакції має бути `income` або `expense`, а категорія й опис — непорожніми.

## Структура проєкту

```text
team-finance-manager/
├── main.py         # інтерактивне меню програми
├── transactions.py # додавання, перегляд, фільтрація та видалення транзакцій
├── financial_statistics.py # підрахунок доходів, витрат і балансу
└── README.md       # опис та інструкція
```

## Запуск

Потрібен Python 3.10 або новіший. Сторонні залежності не потрібні.

```bash
cd team-finance-manager
python3 main.py
```

У меню оберіть дію від `0` до `8`: `1` додає дохід, `2` — витрату, `3` показує транзакції, `4`–`6` показують підсумки, `7` фільтрує за категорією, `8` видаляє транзакцію за ID, а `0` завершує роботу.

## Використання функцій напряму

```python
from transactions import (
    add_transaction,
    delete_transaction,
    filter_by_category,
    show_transactions,
)
from financial_statistics import calculate_balance, calculate_expenses, calculate_income

transactions = []
add_transaction(transactions, "income", 2500, "Зарплата", "Зарплата за жовтень")
add_transaction(transactions, "expense", 350, "Їжа", "Обід")

show_transactions(transactions)
print("Дохід:", calculate_income(transactions))       # 2500
print("Витрати:", calculate_expenses(transactions))   # 350
print("Баланс:", calculate_balance(transactions))     # 2150
print("Їжа:", filter_by_category(transactions, "їжа"))

# ID першої транзакції — 1
transactions, message = delete_transaction(transactions, 1)
print(message)
```

## Обмеження

- Транзакції не зберігаються після завершення програми.
- ID транзакцій — цілі числа, що починаються з `1`.
- ID наступної транзакції збільшується від найбільшого поточного ID.
