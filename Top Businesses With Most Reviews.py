import pandas as pd

# yelp_business[['name', 'review_count']].sort_values(by='review_count', ascending=False).head(5)

yelp_business.nlargest(5, 'review_count')[['name', 'review_count']]
