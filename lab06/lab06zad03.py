import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("diabetes.csv")

#x to set y to label
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2137)


#jak to tutaj przeskalowałem to dokładność jest o 10% wyższa więc super
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(6, 3), activation='relu', max_iter=500, random_state=2137)
mlp.fit(X_train, y_train)


#ewaluacja na zbiorze testowym
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print('Dokładność: {:.2f}%'.format(accuracy*100))
print('Macierz błędu:\n', conf_matrix)


# Dokładność: 76.19%
# Macierz błędu:
#  [[118  20]
#  [ 35  58]]
#poprawnie sklasyfikował 118 przypadków zdrowych pacjentów 
#58 przypadków pacjentów chorujących na cukrzycę
#20 błędów klasyfikując zdrowych jako chorych
#35 błędów - chory jako zdrowy


#co ciekawe bez skalowania danych i random state ustawionym na 42 wychodzi tak:
# Dokładność: 65.37%
# Macierz błędu:
#  [[151   0]
#  [ 80   0]]
#czyli 151 przypadków zdrowych pacjentów 
#0 przypadków pacjentów chorujących na cukrzycę
#0 błędów klasyfikując jako chorych
#80 błędów -chory jako zdrowy
