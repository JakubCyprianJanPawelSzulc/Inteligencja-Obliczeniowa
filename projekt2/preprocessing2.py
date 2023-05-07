import pandas as pd
import numpy as np

data = pd.read_csv('crimedata.csv', sep=',', header=0)
data = data.drop(data.columns[[0, 1, 2, 3]], axis=1)
for column in data.columns:
    data[column] = data[column].interpolate()

data = data.fillna(0)

total_crimes_per_pop = (data["murders"] + data["rapes"] + data["robberies"] + data["assaults"] + data["burglaries"] + data["larcenies"] + data["autoTheft"]) / data["population"] * 100000
data["totalCrimesPerPop"] = total_crimes_per_pop
bins = pd.cut(data['totalCrimesPerPop'], bins=10)
data['crimeRates_categories'] = bins.astype(str)
data = data.drop(data.columns[[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120]], axis=1)
data.to_csv('crimedatapreprocessed2.csv', sep=',', index=False)