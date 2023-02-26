import pandas as pd
import matplotlib.pyplot as plt

#1
#a
miasta = pd.read_csv('miasta.csv')
# print(miasta)
# print(miasta.values)

#b

nowy_wiersz = pd.Series([2010, 460, 555, 405], index=miasta.columns)
miasta = miasta.append(nowy_wiersz, ignore_index=True)

# print(miasta)

#c

# plt.plot(miasta['Rok'], miasta['Gdansk'], marker='o', color='red')
# plt.xlabel('Rok')
# plt.ylabel('Liczba ludności [w tys.]')
# plt.title('Liczba ludności Gdańska w latach 2000-2010')
# plt.show()


#d

axis = miasta.plot(x='Rok', y=list(miasta.columns)[1:], kind='line', marker="o")
axis.set_xlabel('Rok')
axis.set_ylabel('Liczba ludności [w tys.]')
# plt.show()

#e
#standaryzacja danych

miasta = miasta.set_index('Rok')
standard = (miasta - miasta.mean()) / miasta.std()

print(standard)

#srednia

print('srednia: ')
print(standard.mean())

#odchylenie standardowe

print('odchylenie standardowe: ')
print(standard.std())


#f
#normalizacja danych

normal = (miasta - miasta.min()) / (miasta.max() - miasta.min())
print(normal)

#minimum

print('minimum: ')
print(normal.min())

#maksimum

print('maksimum: ')
print(normal.max())



