import pandas as pd

date_range = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
#print(date_range)

data = {'Date': ['2023-01-01','2023-02-15','2023-03-20']} 
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

#print(df[['Date','Day','Month','Year']])

# Weekday and Weekend
df= pd.DataFrame({'Date': pd.date_range(start='2023-01-01', periods=25)})
df['Weekday'] = df['Date'].dt.weekday
df['IsWeekend'] = df['Date'].dt.weekday // 5 == 1

print(df[['Date','Weekday','IsWeekend']])
