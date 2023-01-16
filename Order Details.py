import pandas as pd

df = pd.merge(customers, orders, how='inner', left_on='id', right_on='cust_id')
df[df.first_name.isin(['Jill', 'Eva'])][['first_name', 'order_date', 'order_details', 'total_order_cost']]
