from abc import ABC, abstractmethod
class Expense:
    def __init__(self, name: str, amount: float, account: 'Account'):
        self.name = name
        self.amount = amount
        self.acct = account

    def __str__(self):
        return f"Expense(name={self.name}, amount={self.amount}, will be credited to account {self.acct})"

    @abstractmethod
    def apply(self, funds) -> float:
        pass
        