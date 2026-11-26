"""
Problem 2: Bank Account Class

Условие:
1. Создать класс банковского счёта Account с двумя атрибутами:
   - owner (владелец счёта)
   - balance (баланс счёта)
2. Реализовать строковое представление (__str__), чтобы при print(acct1) выводилось:
   Account owner:   Jose
   Account balance: $100
3. Реализовать два метода:
   - deposit (пополнение счёта: выводит "Deposit Accepted" и возвращает новый баланс)
   - withdraw (снятие со счёта: выводит "Withdrawal Accepted", если денег хватает,
     и "Funds Unavailable!", если сумма снятия превышает текущий баланс).
"""

class Account:

    def __init__(self, owner: str, balance: int | float = 0):
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"

    # Метод пополнения баланса
    def deposit(self, amount: int | float) -> int | float:
        self.balance += amount
        print("Deposit Accepted")
        return self.balance

    # Метод снятия средств с проверкой остатка
    def withdraw(self, amount: int | float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")


if __name__ == "__main__":
    acct1 = Account("Jose", 100)
    print(acct1)
    print(acct1.owner)
    print(acct1.balance)

    print(acct1.deposit(50))
    acct1.withdraw(75)
    acct1.withdraw(500)
