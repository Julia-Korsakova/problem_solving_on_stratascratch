import pandas as pd

df = employee.merge(employee, how='inner', left_on='manager_id', right_on='id')
df[df.salary_x > df.salary_y][['first_name_x', 'salary_x']]
