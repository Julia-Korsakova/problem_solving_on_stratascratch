# Import your libraries
import pandas as pd

# Start writing code
# filter_30 = lyft_drivers[lyft_drivers.yearly_salary <= 30000]
# filter_70 = lyft_drivers[lyft_drivers.yearly_salary >= 70000]
# filter_30.append(filter_70)

lyft_drivers[(lyft_drivers.yearly_salary <= 30000) | (lyft_drivers.yearly_salary >= 70000)]
