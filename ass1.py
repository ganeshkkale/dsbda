import pandas as pd
import numpy as np
df = pd.read_csv('/home/mangal/Downloads/dataset_Facebook.csv', sep = ";")
df.head()
subset1 = df.loc[df["Type"] == "Photo"]
subset1.to_csv('/home/mangal/Downloads/photo_data.csv')
temp = df.iloc[10:25]
print(temp)
df1 = df[['Type', 'Category', 'comment']].loc[4:17]
df2 = df[['Type', 'Category', 'Paid']].loc[24:30]
df3 = df[['Type', 'Category', 'Paid']].loc[31:35]
print("\n", "DF 1 ", df1, "\n")
print("\n", "DF 2 ", df2, "\n")
print("\n", "DF 3 ", df3, "\n")
pd.concat([df1, df2, df3])
df.sort_values(['Category', 'Paid'], ascending=False)
df.transpose()
print(df1)
df_melted = df1.melt (id_vars = None , value_vars = None , ignore_index = False )
print(df_melted)
df_pivoted = df_melted.pivot( columns = 'variable',values = 'value')
print( df_pivoted)