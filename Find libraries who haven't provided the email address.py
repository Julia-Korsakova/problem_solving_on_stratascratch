import pandas as pd

library_usage.head()
df = library_usage[(library_usage.notice_preference_definition == 'email')
    & (library_usage.provided_email_address == False)
    & (library_usage.circulation_active_year == 2016)]
df.home_library_code.unique()
