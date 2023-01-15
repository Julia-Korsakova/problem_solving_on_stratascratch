import pandas as pd

df_heart = facebook_reactions[facebook_reactions['reaction'].str.contains('heart')]['poster']
df = pd.merge(df_heart, facebook_posts, how='inner', left_on = 'poster', right_on = 'post_id').drop_duplicates()
