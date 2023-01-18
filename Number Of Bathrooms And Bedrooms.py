import pandas as pd
import numpy as np

airbnb_search_details.groupby(['city', 'property_type']).agg({'bathrooms': np.mean , 'bedrooms': np.mean})\
    .reset_index()
