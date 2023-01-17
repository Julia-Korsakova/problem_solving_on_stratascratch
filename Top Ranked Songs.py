import pandas as pd

filter_position = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking.position == 1]
filter_position.groupby(['trackname']).agg({'position': 'sum'})\
    .reset_index().sort_values(by='position', ascending = False)