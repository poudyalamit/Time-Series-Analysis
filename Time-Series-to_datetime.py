import pandas as pd
dates = ['2017/05/10 1:29 PM','20220130 13:30','2022 Feb 20','2023.01.29','xyz']
print(pd.to_datetime(dates,format='mixed',errors='coerce')) # gives NaT as output for xyz
print(pd.to_datetime(dates,format='mixed',errors='ignore')) # ignores xyz and set as input

# print(pd.to_datetime('03/12/2023',dayfirst=True))
print(pd.to_datetime('2023#01#20',format='%Y#%m#%d'))

ep_time= 1712420001
print(pd.to_datetime(ep_time, unit='s')) # gives the time and date from the epoch time that started from 1 jan 1970

time = pd.to_datetime(ep_time, unit='s')
print(time.timestamp()) #changes the date time to epoch time