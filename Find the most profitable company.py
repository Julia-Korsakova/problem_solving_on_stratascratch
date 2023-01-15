# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014[forbes_global_2010_2014.sector == 'Financials']\
    .sort_values(by='profits', ascending = False).head(1)[['company', 'continent']]
