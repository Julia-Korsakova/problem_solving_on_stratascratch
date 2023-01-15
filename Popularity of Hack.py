# Import your libraries
import pandas as pd
import numpy as np

df = pd.merge(facebook_employees, facebook_hack_survey, how = 'inner', left_on = 'id', right_on = 'employee_id')
df = df.groupby(['location']).agg({'popularity': np.mean}).reset_index()
