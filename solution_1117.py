import pandas as pd
date1 = pd.Timestamp('2019-01-01', tz='Europe/Berlin')
date2 = pd.Timestamp('2019-01-01', tz='US/Pacific')
date3 = pd.Timestamp('2019-01-01', tz='US/Eastern')
print("Time series data with time zone:")
print(date1)
print(date2)
print(date3)
print("\nTime series data without time zone:")
print(date1.tz_localize(None))
print(date2.tz_localize(None))
print(date3.tz_localize(None))