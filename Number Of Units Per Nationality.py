import pandas as pd

filter_age = airbnb_hosts[airbnb_hosts.age < 30]
filter_apart = airbnb_units[airbnb_units.unit_type == 'Apartment']

df = pd.merge(filter_age, filter_apart, how='inner', left_on='host_id', right_on='host_id').drop_duplicates()
df = df.groupby(['nationality']).agg({'host_id': 'count'}).reset_index()
