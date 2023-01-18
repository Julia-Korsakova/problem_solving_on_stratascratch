import pandas as pd

facebook_complaints.groupby('type').agg({'processed': 'mean'}).reset_index()
