# richman

Personal income allocation tool. Given a monthly income, it distributes funds across a hierarchy of accounts using named expense buckets containing fixed and percentage-based allocations.

## How it works

- **Accounts** hold balances and nest hierarchically (e.g. `Car` → `Car Insurance`, `Car Maintenance`)
- **ConstExpense** deducts a fixed amount and credits the linked account
- **PercentualExpense** deducts a fraction of whatever remains and credits the linked account
- **Buckets** group related expenses and are applied in order — each bucket sees the income left after the previous one

## Run the demo

```
jupyter notebook demo.ipynb
```

## Quick example

```python
from accounts.Account import Account
from expenses.ConstExpense import ConstExpense
from expenses.PercentualExpense import PercentualExpense
from Evaluation import compute_paylisp

safety = Account("Safety")
fun = Account("Fun")

buckets = {
    "Fixed":     [ConstExpense("Rent", 1000, fun)],
    "Remainder": [PercentualExpense("Safety net", 1.0, safety)],
}

compute_paylisp(5000, buckets)
```
