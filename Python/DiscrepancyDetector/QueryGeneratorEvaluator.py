import pickle
from flask import Flask, jsonify, request
app = Flask(__name__)

trained_model = pickle.load(open('query_trained_model.p', 'rb'))

# POST url :  http://127.0.0.1:5000/demoapi/queryevaluator
@app.route('/demoapi/queryevaluator/', methods = ['POST'])
def queryevaluator():
    request_json = request.get_json()
    age  = float(request_json.get('age'))
    bodyweight  = float(request_json.get('bodyweight'))
    
    test_data = [age, bodyweight]
    test_result = trained_model.predict([test_data])[0]

    possible_outcomes = ['Data is Ok', 'Weight is high compared to age']
    return jsonify({'data_validation_status': possible_outcomes[test_result]})

# driver function
# To stop server run in terminal > taskkill /f /im python.exe
if __name__ == '__main__':  
    app.run()





