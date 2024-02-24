import pandas as pd
import numpy as np

mySeries = pd.Series([1, 7, "Aman", 8, 9, 11, 13, "CEU", 23, "Python"])
print(mySeries)
print(type(mySeries))

# Assigning a custom index to the series
SongsSeries = pd.Series(
  data = ["Cruel Summer",
         "Hold My Hand",
         "The Show"],
  index = ["Taylor Swift",
          "Lady Gaga",
          "Lenka"]
)
print(SongsSeries)

# Advanced indexing
print(SongsSeries.loc["Taylor Swift"])
#Alternatively:
print(SongsSeries.iloc[0])

print(SongsSeries.loc[["Lady Gaga", "Lenka"]])

#Access a particular element from the series
print(SongsSeries.loc["Taylor Swift":"Lenka"])