from .Expense import Expense

class ConstExpense(Expense):
    def __str__(self):
        return f"Const {super().__str__()}"
        
    def apply(self, funds) -> float:
        if funds < self.amount:
            print(f"{self.__str__()} can't be applied with {funds} income")
            return 0

        self.acct.credit(self.amount)
        return self.amount
