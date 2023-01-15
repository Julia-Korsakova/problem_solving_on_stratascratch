import pandas as pd
import numpy as np

avg_salary_dep = employee.groupby(['department']).agg({'salary': np.mean}).reset_index()
new_df = pd.merge(employee, avg_salary_dep, how='inner', left_on='department', right_on='department')
new_df = new_df[['department', 'first_name', 'salary_x', 'salary_y']]
