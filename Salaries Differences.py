import pandas as pd
import numpy as np

filter_engineering = np.max(db_employee[db_employee.department_id == 1].salary)
filter_marketing = np.max(db_employee[db_employee.department_id == 4].salary)

pd.DataFrame({'salary_difference':[abs(filter_marketing - filter_engineering)]})
