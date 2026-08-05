"""
generate_data.py
Generates a realistic synthetic e-commerce transactional dataset
for the RFM Customer Segmentation project.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

N_CUSTOMERS = 600
END_DATE = datetime(2026, 6, 30)
START_DATE = END_DATE - timedelta(days=365)

customer_ids = [f"CUST{str(i).zfill(4)}" for i in range(1, N_CUSTOMERS + 1)]

# Give each customer a "behavior profile" so segments emerge naturally
profiles = np.random.choice(
    ["loyal", "regular", "new", "at_risk", "churned"],
    size=N_CUSTOMERS,
    p=[0.15, 0.30, 0.15, 0.20, 0.20]
)

rows = []
order_id = 1

for cust, profile in zip(customer_ids, profiles):
    if profile == "loyal":
        n_orders = np.random.randint(15, 30)
        recency_days = np.random.randint(1, 20)
        amount_range = (800, 5000)
    elif profile == "regular":
        n_orders = np.random.randint(6, 14)
        recency_days = np.random.randint(10, 60)
        amount_range = (400, 2500)
    elif profile == "new":
        n_orders = np.random.randint(1, 3)
        recency_days = np.random.randint(1, 30)
        amount_range = (300, 1500)
    elif profile == "at_risk":
        n_orders = np.random.randint(4, 10)
        recency_days = np.random.randint(90, 160)
        amount_range = (300, 2000)
    else:  # churned
        n_orders = np.random.randint(1, 6)
        recency_days = np.random.randint(200, 360)
        amount_range = (200, 1800)

    last_purchase = END_DATE - timedelta(days=int(recency_days))

    for _ in range(n_orders):
        days_before_last = np.random.randint(0, 300)
        order_date = last_purchase - timedelta(days=int(days_before_last))
        if order_date < START_DATE:
            order_date = START_DATE + timedelta(days=np.random.randint(0, 30))

        amount = round(np.random.uniform(*amount_range), 2)

        rows.append({
            "OrderID": order_id,
            "CustomerID": cust,
            "OrderDate": order_date.strftime("%Y-%m-%d"),
            "Amount": amount
        })
        order_id += 1

df = pd.DataFrame(rows)
df = df.sort_values("OrderDate").reset_index(drop=True)

output_path = "data/transactions.csv"
df.to_csv(output_path, index=False)
print(f"Generated {len(df)} transactions for {N_CUSTOMERS} customers -> {output_path}")
