import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)
print(train_set)

def classify_iris(sl, sw, pl, pw):
    if sl >= 4.3 and sl <= 5.8 and sw >= 2.3 and sw <= 4.4 and pl >= 1 and pl <= 1.9 and pw >= 0.1 and pw <= 0.6:
        return("setosa")
    elif sl >= 4.9 and sl <= 7 and sw >= 2 and sw <= 3.4 and pl >= 3 and pl <= 5.1 and pw >= 1 and pw <= 1.8:
        return("versicolor")
    elif sl >= 4.9 and sl <= 7.9 and sw >= 2.2 and sw <= 3.8 and pl >= 4.5 and pl <= 6.9 and pw >= 1.4 and pw <= 2.5:
        return("virginica")
    else:
        return("nieznany gatunek")

    
good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    if classify_iris(test_set[i,0], test_set[i,1], test_set[i,2], test_set[i,3]) == test_set[i,4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/len*100, "%")