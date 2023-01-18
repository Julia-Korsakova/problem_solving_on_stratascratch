import pandas as pd

df_worker = worker[worker.salary == worker.salary.max()][['worker_id', 'salary']]
df_worker.merge(title, how='inner', left_on='worker_id', right_on='worker_ref_id')['worker_title']
