import pandas as pd

airbnb_hosts.merge(airbnb_guests, how='inner', on=['nationality', 'gender'])[['host_id', 'guest_id']].drop_duplicates()
