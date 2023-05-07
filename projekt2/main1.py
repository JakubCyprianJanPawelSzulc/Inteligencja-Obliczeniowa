import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import StandardScaler
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt

df = pd.read_csv("crimedatapreprocessed1.csv")


X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2137)

label_encoder = LabelEncoder()
y_all = label_encoder.fit_transform(np.concatenate([y_train, y_test]))
y_train = y_all[:len(y_train)]
y_test = y_all[len(y_train):]


dtc_small = DecisionTreeClassifier(max_depth=5, random_state=2137)
dtc_large = DecisionTreeClassifier(random_state=2137)
gnb = GaussianNB()
knn = KNeighborsClassifier(n_neighbors=10)
knn2 = KNeighborsClassifier(n_neighbors=20)
knn3 = KNeighborsClassifier(n_neighbors=30)
mlp = MLPClassifier(hidden_layer_sizes=(10,7), max_iter=1000, random_state=2137)
mlp2 = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=2137)
mlp3 = MLPClassifier(hidden_layer_sizes=(10,7,5), max_iter=1000, random_state=2137)

dtc_small.fit(X_train, y_train)
dtc_large.fit(X_train, y_train)
gnb.fit(X_train, y_train)
knn.fit(X_train, y_train)
knn2.fit(X_train, y_train)
knn3.fit(X_train, y_train)
mlp.fit(X_train, y_train)
mlp2.fit(X_train, y_train)
mlp3.fit(X_train, y_train)

y_pred_dtc_small = dtc_small.predict(X_test)
y_pred_dtc_large = dtc_large.predict(X_test)
y_pred_gnb = gnb.predict(X_test)
y_pred_knn = knn.predict(X_test)
y_pred_knn2 = knn2.predict(X_test)
y_pred_knn3 = knn3.predict(X_test)
y_pred_mlp = mlp.predict(X_test)
y_pred_mlp2 = mlp2.predict(X_test)
y_pred_mlp3 = mlp3.predict(X_test)

cm_dtc_small = confusion_matrix(y_test, y_pred_dtc_small)
cm_dtc_large = confusion_matrix(y_test, y_pred_dtc_large)
cm_gnb = confusion_matrix(y_test, y_pred_gnb)
cm_knn = confusion_matrix(y_test, y_pred_knn)
cm_knn2 = confusion_matrix(y_test, y_pred_knn2)
cm_knn3 = confusion_matrix(y_test, y_pred_knn3)
cm_mlp = confusion_matrix(y_test, y_pred_mlp)
cm_mlp2 = confusion_matrix(y_test, y_pred_mlp2)
cm_mlp3 = confusion_matrix(y_test, y_pred_mlp3)

print('Dokładność dtc_small: {:.2f}%'.format(accuracy_score(y_test, y_pred_dtc_small)*100))
# print('Macierz błędu:\n', cm_dtc_small)
print('Dokładność dtc_large: {:.2f}%'.format(accuracy_score(y_test, y_pred_dtc_large)*100))
# print('Macierz błędu:\n', cm_dtc_large)
print('Dokładność gnb: {:.2f}%'.format(accuracy_score(y_test, y_pred_gnb)*100))
# print('Macierz błędu:\n', cm_gnb)
print('Dokładność knn: {:.2f}%'.format(accuracy_score(y_test, y_pred_knn)*100))
# print('Macierz błędu:\n', cm_knn)
print('Dokładność knn2: {:.2f}%'.format(accuracy_score(y_test, y_pred_knn2)*100))
# print('Macierz błędu:\n', cm_knn2)
print('Dokładność knn3: {:.2f}%'.format(accuracy_score(y_test, y_pred_knn3)*100))
# print('Macierz błędu:\n', cm_knn3)
print('Dokładność mlp: {:.2f}%'.format(accuracy_score(y_test, y_pred_mlp)*100))
# print('Macierz błędu:\n', cm_mlp)
print('Dokładność mlp2: {:.2f}%'.format(accuracy_score(y_test, y_pred_mlp2)*100))
# print('Macierz błędu:\n', cm_mlp2)
print('Dokładność mlp3: {:.2f}%'.format(accuracy_score(y_test, y_pred_mlp3)*100))
# print('Macierz błędu:\n', cm_mlp3)

