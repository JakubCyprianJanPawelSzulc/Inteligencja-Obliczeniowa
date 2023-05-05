import pandas as pd
import numpy as np

data = pd.read_csv('crimedata.csv', sep=',', header=0)
threshold = len(data) * 0.5
data = data.dropna(thresh=threshold, axis=1)
data.to_csv('crimedatapreprocessed1.csv', sep=',', index=False)

