# Import your libraries
import pandas as pd

# Start writing code
df = dc_bikeshare_q1_2012.groupby(['bike_number']).agg({'end_time': 'max'}).reset_index()
df.sort_values(by='end_time', ascending = False)[['bike_number', 'end_time']]
