import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

csv_path = r'C:\Users\Eric\Desktop\Programming Files\Wordcount Tool\Wordcount_records.csv'

df = pd.read_csv(csv_path)

print(df.head())

df.set_index(['Date'])

fig = sns.barplot(x='Date', y='Wordcount', data=df)

# print(df.head())

plt.show()

