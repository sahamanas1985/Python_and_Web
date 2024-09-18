import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import GridSearchCV


dffull = pd.read_csv(r"covid_trainer_data.csv")

# drop text columns
df = dffull.drop(['Result_description'], axis='columns')

X_train, X_test, y_train, y_test = train_test_split(df.drop(['Result'], axis='columns'), \
    df.Result, test_size=0.2)

# K fold cross method for model selection


score_rf = cross_val_score(RandomForestClassifier(n_estimators=50), df.drop(['Result'], axis='columns'), \
    df.Result, cv=3)

#print(score_rf)

'''

score_lr = cross_val_score(LogisticRegression(solver='lbfgs', max_iter=10), df.drop(['Result'], axis='columns'), \
    df.Result, cv=3)

print(score_lr)

'''

# hyper parameter tuning

clf = GridSearchCV(RandomForestClassifier(), {
    'n_estimators':[30, 35, 40, 45, 50]
}, cv=3, return_train_score=False)

clf.fit(df.drop(['Result'], axis='columns'), df.Result)


pd.set_option('display.max_columns', 20)
df = pd.DataFrame(clf.cv_results_)
print(df[['param_n_estimators', 'mean_fit_time', 'mean_test_score', 'rank_test_score']])