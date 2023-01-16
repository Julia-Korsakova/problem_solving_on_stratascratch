import pandas as pd
import numpy as np

airbnb_search_details.groupby(['city', 'property_type']).agg({'bedrooms': np.mean, 'beds': np.mean}).reset_index()
