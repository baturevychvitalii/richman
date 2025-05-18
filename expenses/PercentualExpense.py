from .Expense import Expense

class PercentualExpense(Expense):
    def __str__(self):
        return f"Variable {super().__str__()}"
        
    def apply(self, funds) -> float:
        if funds < 0:
            print(f"{self.__str__()} can't be applied with {funds} income")
            return 0

        self.acct.credit(funds * self.amount)
        return funds * self.amount
