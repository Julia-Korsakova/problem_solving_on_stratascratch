import pandas as pd
import numpy as np

filter_mbp = playbook_events[playbook_events.device == 'macbook pro']
filter_mbp.groupby(['event_name']).agg({'device': np.count_nonzero}).reset_index()
