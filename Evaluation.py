def compute_paylisp(month, income, expenseBuckets):
    print(f"Computing paylisp for {month}\n\n")
    
    for name, bucket in expenseBuckets.items():
        bucket_spend = 0
        for expense in bucket:
            bucket_spend += expense.apply(income)
        income -= bucket_spend
        print(f"{name} bucket spending {bucket_spend}")
        
    print(f"Leftover income: {income}\n")
    
            