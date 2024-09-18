import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

print ("Reading training data from CSV")
df = pd.read_csv(r"bodytemp.csv")

data = df.values

#print(dataframe['Body_temp'].describe())

#plt.scatter(df['Patient_id'].values, df['Body_temp'].values)
#plt.xlabel('Patient Id')
#plt.ylabel('Body Temp')
#plt.title("Body temparature distribution")
#plt.show()


model=IsolationForest(n_estimators=50, max_samples='auto', contamination=float(0.1),max_features=1.0)
model.fit(df[['Body_temp']])

df['scores']=model.decision_function(df[['Body_temp']])
df['anomaly']=model.predict(df[['Body_temp']])

#print(df)

anomaly=df.loc[df['anomaly']==-1]
anomaly_index=list(anomaly.index)
print(anomaly)


