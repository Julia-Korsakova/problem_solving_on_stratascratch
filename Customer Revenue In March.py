import pandas as pd

df = orders[orders.order_date.dt.month == 3]
df.groupby('cust_id').agg({'total_order_cost': 'sum'}).reset_index()\
    .sort_values('total_order_cost', ascending=False)
