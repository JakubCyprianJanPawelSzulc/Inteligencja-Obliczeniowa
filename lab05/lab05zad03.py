import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("iris.csv")

train_set, test_set = train_test_split(df, train_size=0.7, random_state=13)

train_input = train_set.iloc[:, :-1]
train_class = train_set.iloc[:, -1]
test_input = test_set.iloc[:, :-1]
test_class = test_set.iloc[:, -1]

print("Zbiór treningowy:")
print(train_set)
print("Zbiór testowy:")
print(test_set)

classifier = DecisionTreeClassifier()
classifier.fit(train_input, train_class)

accuracy = classifier.score(test_input, test_class)
print(f"Dokładność klasyfikatora: {accuracy * 100:.2f}%")

predicted_class = classifier.predict(test_input)

confusion_mat = confusion_matrix(test_class, predicted_class)
print("Macierz błędów:")
print(confusion_mat)


