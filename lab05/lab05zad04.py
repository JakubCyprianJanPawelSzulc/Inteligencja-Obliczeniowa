from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Klasyfikator 1: 1-NN (dominanta)
y_pred_dd = []
for sample in X_test:
    min_dist = float("inf")
    nearest = None
    for i, train_sample in enumerate(X_train):
        dist = sum([(a - b) ** 2 for a, b in zip(sample, train_sample)]) ** 0.5
        if dist < min_dist:
            min_dist = dist
            nearest = i
    y_pred_dd.append(y_train[nearest])
acc_dd = accuracy_score(y_test, y_pred_dd)
cm_dd = confusion_matrix(y_test, y_pred_dd)

# Klasyfikator 2: k-NN, k=3
knn3 = KNeighborsClassifier(n_neighbors=3)
knn3.fit(X_train, y_train)
y_pred_knn3 = knn3.predict(X_test)
acc_knn3 = accuracy_score(y_test, y_pred_knn3)
cm_knn3 = confusion_matrix(y_test, y_pred_knn3)

# Klasyfikator 3: k-NN, k=5
knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(X_train, y_train)
y_pred_knn5 = knn5.predict(X_test)
acc_knn5 = accuracy_score(y_test, y_pred_knn5)
cm_knn5 = confusion_matrix(y_test, y_pred_knn5)

# Klasyfikator 4: k-NN, k=11
knn11 = KNeighborsClassifier(n_neighbors=11)
knn11.fit(X_train, y_train)
y_pred_knn11 = knn11.predict(X_test)
acc_knn11 = accuracy_score(y_test, y_pred_knn11)
cm_knn11 = confusion_matrix(y_test, y_pred_knn11)

# Klasyfikator 5: Naive Bayes
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
acc_nb = accuracy_score(y_test, y_pred_nb)
cm_nb = confusion_matrix(y_test, y_pred_nb)

print(f"Dokładność dla DD: {acc_dd*100:.2f}%")
print(f"Macierz błędów dla DD:\n{cm_dd}\n")

print(f"Dokładność dla k-NN, k=3: {acc_knn3*100:.2f}%")
print(f"Macierz błędów dla k-NN, k=3:\n{cm_knn3}\n")

print(f"Dokładność dla k-NN, k=5: {acc_knn5*100:.2f}%")
print(f"Macierz błędów dla k-NN, k=5:\n{cm_knn5}\n")

print(f"Dokładność dla k-NN, k=11: {acc_knn11*100:.2f}%")
print(f"Macierz błędów dla k-NN, k=11:\n{cm_knn11}\n")

print(f"Dokładność dla Naive Bayes: {acc_nb*100:.2f}%")
print(f"Macierz błędów dla Naive Bayes:\n{cm_nb}\n")