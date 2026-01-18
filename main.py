from models.transaction import Transaction
from models.category import Category


# Пример использования
if __name__ == "__main__":
    t1 = Transaction(100, "Food", "2023-10-25")
    print(t1)

if __name__ == "__main__":
    t1 = Category("Food", "Category for food expenses")
    print(t1)
