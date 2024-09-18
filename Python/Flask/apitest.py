from flask import Flask, jsonify, request
app = Flask(__name__)

# GET url :  http://127.0.0.1:5000/demoapi/addnumbers/?num1=10&num2=5
@app.route('/demoapi/addnumbers/', methods = ['GET'])
def addnumbers():
    num1  = request.args.get('num1', None)
    num2  = request.args.get('num2', None)
    num3 = float(num1) + float(num2)
    return jsonify({'sum': num3})

# POST url :  http://127.0.0.1:5000/demoapi/multiplynumbers/
@app.route('/demoapi/multiplynumbers/', methods = ['POST'])
def multiplynumbers():
    request_json = request.get_json()
    num1  = request_json.get('num1')
    num2  = request_json.get('num2')
    num3 = float(num1) * float(num2)
    return jsonify({'multiplication': num3})
  
  
# driver function
# To stop server run in terminal > taskkill /f /im python.exe
if __name__ == '__main__':  
    app.run()