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


df = pd.read_csv("crimedatapreprocessed1.csv")


X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2137)

label_encoder = LabelEncoder()
y_all = label_encoder.fit_transform(np.concatenate([y_train, y_test]))
y_train = y_all[:len(y_train)]
y_test = y_all[len(y_train):]

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

normalizer=MinMaxScaler()
normalizer.fit(X_train)
X_train=normalizer.transform(X_train)
X_test=normalizer.transform(X_test)


dtc_small = DecisionTreeClassifier(max_depth=5, random_state=2137)
dtc_large = DecisionTreeClassifier(random_state=2137)
gnb = GaussianNB()
knn = KNeighborsClassifier(n_neighbors=10)
mlp = MLPClassifier(hidden_layer_sizes=(10,7), max_iter=1000, random_state=2137)

dtc_small.fit(X_train, y_train)
dtc_large.fit(X_train, y_train)
gnb.fit(X_train, y_train)
knn.fit(X_train, y_train)
mlp.fit(X_train, y_train)

y_pred_dtc_small = dtc_small.predict(X_test)
y_pred_dtc_large = dtc_large.predict(X_test)
y_pred_gnb = gnb.predict(X_test)
y_pred_knn = knn.predict(X_test)
y_pred_mlp = mlp.predict(X_test)

cm_dtc_small = confusion_matrix(y_test, y_pred_dtc_small)
cm_dtc_large = confusion_matrix(y_test, y_pred_dtc_large)
cm_gnb = confusion_matrix(y_test, y_pred_gnb)
cm_knn = confusion_matrix(y_test, y_pred_knn)
cm_mlp = confusion_matrix(y_test, y_pred_mlp)

print('Dokładność dtc_small: {:.2f}%'.format(accuracy_score(y_test, y_pred_dtc_small)*100))
# print('Macierz błędu:\n', cm_dtc_small)
print('Dokładność dtc_large: {:.2f}%'.format(accuracy_score(y_test, y_pred_dtc_large)*100))
# print('Macierz błędu:\n', cm_dtc_large)
print('Dokładność gnb: {:.2f}%'.format(accuracy_score(y_test, y_pred_gnb)*100))
# print('Macierz błędu:\n', cm_gnb)
print('Dokładność knn: {:.2f}%'.format(accuracy_score(y_test, y_pred_knn)*100))
# print('Macierz błędu:\n', cm_knn)
print('Dokładność mlp: {:.2f}%'.format(accuracy_score(y_test, y_pred_mlp)*100))
# print('Macierz błędu:\n', cm_mlp)

