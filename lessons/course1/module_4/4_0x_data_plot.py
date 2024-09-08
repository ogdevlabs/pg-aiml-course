import matplotlib.pyplot as plt
import pandas as pd

file_path = '../../../files/titanic_train.csv'
with open(file_path,'r') as file:
    content = file.read()
    print(content)

df_csv = pd.read_csv(file_path)

df = pd.read_csv(file_path)
df.head()

plt.scatter(df['Age'], df['Fare'])
plt.show()