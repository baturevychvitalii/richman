from typing import List
class Account:
    def __init__(self, name: str, amount: float=0, sub_accounts: List['Account']=None):
        """
        Initialize an Account object.

        :param name: The name of the account.
        :param amount: The amount associated with the account.
        :param sub_accounts: An optional list of sub-accounts (default is None).
        """
        self.name = name
        self.amount = amount
        self.sub_accounts = sub_accounts if sub_accounts is not None else []
        self.parent = None

    def add_sub_account(self, acc: 'Account'):
        self.sub_accounts.append(acc)
        acc.parent = self
    
    def add_sub_accounts(self, sub_accounts: List['Account']):
        for acc in sub_accounts:
            self.add_sub_account(acc)

    def __str__(self):
        return f"{self.name} -> {self.amount} {f"(total: {self.total_amount()})" if self.sub_accounts else ''}"

    def recursive_print(self, delim=""):
        print(delim, self)
        if self.sub_accounts:
            print(delim, "\\")
            for acc in self.sub_accounts:
                acc.recursive_print(delim + " ")

    def total_amount(self) -> float:
        """Calculate the total amount including sub-accounts."""
        total = self.amount
        for sub_account in self.sub_accounts:
            total += sub_account.total_amount()
        return total

    def credit(self, income):
        self.amount += income
