# richman

Personal income-allocation tool written in Python + Jupyter.

## Purpose

Given a monthly income, distribute it across a hierarchy of named accounts using ordered expense buckets.

## Module map

```
Evaluation.py                  — compute_paylisp(income, buckets): runs all buckets, prints summary
accounts/Account.py            — Account: hierarchical account with credit(), total_amount(), recursive_print()
expenses/Expense.py            — Abstract base: Expense(name, amount, account)
expenses/ConstExpense.py       — Fixed-amount deduction → credits linked account
expenses/PercentualExpense.py  — Percentage of remaining funds → credits linked account
demo.ipynb                     — Public reference notebook with fictional data
main.ipynb                     — (git-ignored) Real personal notebook with actual financial data
```

## How the layers fit together

1. **Account** objects form a tree; sub-accounts track detailed breakdowns
2. **Expense** subclasses each implement `apply(funds) → amount_spent`, crediting their linked account
3. **compute_paylisp** iterates buckets in order, reducing remaining income after each one

## Notes

- `main.ipynb` is git-ignored — it contains real personal data. `demo.ipynb` is the public reference.
- No external dependencies beyond Python standard library and Jupyter.
