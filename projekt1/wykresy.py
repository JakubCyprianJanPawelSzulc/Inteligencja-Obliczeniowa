import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('zeit1.csv', header=None)
df2 = pd.read_csv('zeit2.csv', header=None)
df3 = pd.read_csv('zeit3.csv', header=None)

df1 = df1[df1[0] != 0]
df2 = df2[df2[0] != 0]
df3 = df3[df3[0] != 0]

plt.plot(df1[0], label='Dane 1')
plt.plot(df2[0], label='Dane 2')
plt.plot(df3[0], label='Dane 3')

plt.legend()
plt.ylabel('Czasy wykonywania')

plt.show()
