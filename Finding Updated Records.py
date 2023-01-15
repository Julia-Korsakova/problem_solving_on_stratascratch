import pandas as pd
import numpy as np

ms_employee_salary.head()
ms_employee_salary.groupby(['id', 'first_name', 'last_name', 'department_id']).agg({'salary': np.max}).reset_index()
