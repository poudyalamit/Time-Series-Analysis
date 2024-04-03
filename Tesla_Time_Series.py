import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tesla.csv", parse_dates=["Date"], index_col="Date");
# print(type(df.Date[0])) #checking the type of the date 
# print(df.index) # after indexing the column Date
# print(df.head(10)); #to print the 10 datas from top

df.plot(ylabel="Price in USD")
print(df.loc["2023-01" : "2023-05"].mean()) #mean of the interval of time
df.loc["2023-01" : "2023-05"].plot(title="Tesla Time Series 2023",ylabel="Price in USD") # for an interval of time
print(df.loc["2023"].resample("ME").mean()) #resampling to the month format
df.loc["2023"].resample("ME").mean().plot(title="Tesla Time Series monthly-23",ylabel="Price in USD")
plt.show()
