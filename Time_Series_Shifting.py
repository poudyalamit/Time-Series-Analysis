import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('./data/tesla.csv',parse_dates=['Date'],index_col='Date')
# print(df.head())
# df.plot()
# df.shift(30).plot() #shifting right
# df.shift(-30).plot() #shifting left

df['prev day close']= df['Close'].shift(1)
df['1 day Change']= df['Close'] - df['prev day close']
print(df)
plt.show()