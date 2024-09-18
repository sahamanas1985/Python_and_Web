import pickle
from sklearn.neighbors import KNeighborsClassifier

trained_model = pickle.load(open('patient_model.trn', 'rb'))

testuser_temparature = 98
testuser_cough_severity = 1

test_data = [testuser_temparature, testuser_cough_severity]
test_result = trained_model.predict([test_data])[0]

possible_outcomes = ['Healthy', 'Cough', 'Fever', 'Flu', 'Covid 19']

print('Patient condition is: ' + possible_outcomes[test_result])