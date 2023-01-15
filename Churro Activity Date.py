import pandas as pd
import numpy as np

# los_angeles_restaurant_health_inspections.head()
df = los_angeles_restaurant_health_inspections[(los_angeles_restaurant_health_inspections.facility_name == 'STREET CHURROS') & (los_angeles_restaurant_health_inspections.score < 95)][['activity_date', 'pe_description']]
df.activity_date = df.activity_date.astype(str)
# type(los_angeles_restaurant_health_inspections.activity_date[0])
