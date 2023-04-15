from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)


le = LabelEncoder()
train_labels = le.fit_transform(y_train)
test_labels = le.transform(y_test)

print(le.classes_)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


mlp = MLPClassifier(hidden_layer_sizes=(2,), max_iter=1000)
mlp.fit(X_train_scaled, train_labels)

score = mlp.score(X_test_scaled, test_labels)
print(score)

mlp_3 = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1000)
mlp_3.fit(X_train_scaled, train_labels)
score_3 = mlp_3.score(X_test_scaled, test_labels)
print(score_3)

mlp_2layers = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=1000)
mlp_2layers.fit(X_train_scaled, train_labels)
score_2layers = mlp_2layers.score(X_test_scaled, test_labels)
print(score_2layers)