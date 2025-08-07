import pandas as pd

import os
print("Current working directory:", os.getcwd())
titanic_df = pd.read_csv(r'..\..\..\Data\titanic.csv')

print(titanic_df['Age'])