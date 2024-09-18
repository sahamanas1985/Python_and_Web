import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier

print ("reading training data from CSV")
data = pd.read_csv(r"TrainingData.csv")

input_col_headers = ['Body_Temp', 'Cough_Severity']
input_col = data[input_col_headers]
result_col = data['Result']

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(input_col.values, result_col.values)

pickle.dump(knn, open('patient_model.trn', 'wb'))

print("Model Trained and saved successfully!")