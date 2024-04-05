import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('./data/nifty_50.csv')
# print(df.head(10));

range = pd.date_range(start="01/03/2022",end="01/31/2022",freq="B") #periods are also used to generate days
# print(range)

df.set_index(range,inplace=True) 
# print(df)
df.drop(axis="index",index="2022-01-26",inplace=True) #dropped the data of the data frame of missing value
# print(df)

# df.Close.plot()
# plt.show()

print(df.asfreq(freq="D",method="pad")) # to convert time series to the given frequency
