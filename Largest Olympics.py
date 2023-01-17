# Import your libraries
import pandas as pd

olympics_athletes_events.drop_duplicates('name').groupby(['games']).agg({'sport': 'count'})\
    .reset_index().nlargest(1, 'sport')
