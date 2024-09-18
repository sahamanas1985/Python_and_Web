import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

#Read Training Data from the input Excel and prepare Dataframe.
print ("Reading training data from Excel...")
data = pd.read_excel('covid_trainer_data.xlsx', sheet_name='covid_trainer_data')

input_col_headers = ['Body_Temp', 'Cough_Severity', 'SPO2']
input_col = data[input_col_headers]
result_col = data['Result']

dtc = DecisionTreeClassifier()
dtc.fit(input_col.values, result_col.values)

pickle.dump(dtc, open('covid_trained_model.p', 'wb'))

print("Model Trained and saved successfully!")