import pandas as pd

pd.merge(customers, orders, how='left', left_on='id', right_on='cust_id')\
    [['first_name', 'last_name', 'city', 'order_details']].sort_values(by=['first_name', 'order_details'])
