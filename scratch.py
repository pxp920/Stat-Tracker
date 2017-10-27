import pandas as pd

df = pd.read_csv("C:/Users/Panagiotis.Pantazis/Documents/Python Scripts/Stat Tracker/ScoreTracking.csv", header=0,
                 encoding='ANSI')

print(list(df))

print(df.loc(1))