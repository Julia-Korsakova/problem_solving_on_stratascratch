import pandas as pd

filter_year = billboard_top_100_year_end[billboard_top_100_year_end.year == 2010]
filter_year.sort_values('year_rank').drop_duplicates('song_name')[['year_rank', 'group_name', 'song_name']].head(10)
