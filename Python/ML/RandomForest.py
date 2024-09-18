import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn


dffull = pd.read_csv(r"covid_trainer_data.csv")

# drop text columns
df = dffull.drop(['Result_description'], axis='columns')
#print(dfcleaned)

X_train, X_test, y_train, y_test = train_test_split(df.drop(['Result'], axis='columns'), \
    df.Result, test_size=0.2)

#print(len(X_test))

model = RandomForestClassifier(n_estimators=50)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(score)

y_predicted = model.predict(X_test)

# print confuson matrix > (truth, predicted)
cm = confusion_matrix(y_test, y_predicted)

plt.figure(figsize=(5,5))
sn.heatmap(cm, annot=True)
plt.xlabel("Predicted")
plt.ylabel("Truth")
plt.show()

