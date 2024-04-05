import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday,Holiday
df= pd.read_csv('./data/apple_stock.csv')
# print(df.head(10));

# print(pd.date_range(start="03/01/2022",end="01/01/2024",freq="B"))

USbd= CustomBusinessDay(calendar=USFederalHolidayCalendar())
# print(USbd)

rng= pd.date_range(start="01/02/2024",end="03/28/2024",freq=USbd)
# print(rng)

df.set_index(rng,inplace=True)
# print(df)


# can be used to make own holidaycalendar and can explore more in pandas docs at timeseries-holiday 
class Wasingtonb (AbstractHolidayCalendar):
    rules=[
        Holiday("Wasington's Birthday",month=2, day=20,observance= nearest_workday)
    ]
wb = CustomBusinessDay(calendar=Wasingtonb())
rangs= pd.date_range(start="01/02/2024",end="03/28/2024",freq=wb)
print(rangs)

# for the custombussiness day with weekend fri and sat
bd = CustomBusinessDay(weekmask= 'Sun Mon Tue Wed Thu'#,holidays= "Date of holiday"
)
range= pd.date_range(start="01/02/2024",end="03/28/2024",freq=bd)
print(range)