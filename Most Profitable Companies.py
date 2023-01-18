import pandas as pd

forbes_global_2010_2014.nlargest(3, 'profits')[['company', 'profits']]
