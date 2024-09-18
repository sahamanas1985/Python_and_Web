import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

#Read Training Data from the input Excel and prepare Dataframe.
print ("Reading sample data from Excel...")
data = pd.read_excel('query_data.xlsx', sheet_name='Sheet1')

input_col_headers = ['Age', 'Weight']
input_col = data[input_col_headers]
result_col = data['Query']

dtc = DecisionTreeClassifier()
dtc.fit(input_col.values, result_col.values)

pickle.dump(dtc, open('query_trained_model.p', 'wb'))

print("Model Trained and saved successfully!")