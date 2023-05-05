import pandas as pd
import numpy as np

data = pd.read_csv('crimedata.csv', sep=',', header=0)
data.fillna(0, inplace=True)
data.to_csv('crimedatapreprocessed2.csv', sep=',', index=False)