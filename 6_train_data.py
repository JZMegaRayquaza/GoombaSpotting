import os
import pandas as pd

csv_file = 'goomba_spotting.csv'
df = pd.read_csv(csv_file)

print(df.head())
