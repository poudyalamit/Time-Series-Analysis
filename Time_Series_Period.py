import pandas as pd

# yr=pd.Period('2017')
# print(yr.start_time)
# print(yr.end_time)

# month = pd.Period('2018-12',freq='M')
# print(month.start_time)
# print(month.end_time)
# print(month+1)

# day = pd.Period('2016-02-28',freq='D')
# print(day.start_time)
# print(day.end_time)
# print(day+1)


# hour = pd.Period('2017-02-02 23:00',freq='h')
# print(hour+ pd.offsets.Hour(3))

indx = pd.period_range('2012','2017',freq='Q')
print(indx)

index = pd.period_range('2012','2017',freq='Q-JAN')
print(index[0].start_time)
print(index[0].end_time)
print(index.start_time)
print(index.end_time)

idx = pd.period_range('2012',periods=10,freq='Q-JAN')
print(idx)

dt = idx.to_timestamp()
print(dt)

print(dt.to_period())