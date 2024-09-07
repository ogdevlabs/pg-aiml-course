import pandas as pd

file_path = '../../../files/titanic_train_copy.csv'
with open(file_path,'r') as file:
    content = file.read()
    print(content)
    
df_csv = pd.read_csv(file_path)
print(df_csv)