import pickle
from flask import Flask, jsonify, request
app = Flask(__name__)

trained_model = pickle.load(open('covid_trained_model.p', 'rb'))

# POST url :  http://127.0.0.1:5000/demoapi/covidpredictor/
@app.route('/demoapi/covidpredictor/', methods = ['POST'])
def covidpredictor():
    request_json = request.get_json()
    temparature  = float(request_json.get('temparature'))
    coughseverity  = float(request_json.get('coughseverity'))
    spo2  = float(request_json.get('spo2'))

    test_data = [temparature, coughseverity, spo2]
    test_result = trained_model.predict([test_data])[0]

    possible_outcomes = ['Healthy', 'Cough', 'Flu', 'Covid', 'Fever']
    return jsonify({'predicted_condition': possible_outcomes[test_result]})

# driver function
# To stop server run in terminal > taskkill /f /im python.exe
if __name__ == '__main__':  
    app.run()