import operator
import pandas as pd
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# POST url :  http://127.0.0.1:5000/demoapi/fuzzysearch/
@app.route('/demoapi/fuzzysearch/', methods = ['POST'])
def fuzzysearch():
    request_json = request.get_json()
    TextToCompare  = request_json.get('searchtext')
    
    #read CSV and convert content into 1D Array
    df = pd.read_csv(r"CompanyNames.csv")
    datalist = df.values.ravel()
    
    #Use different Fuzz algorithms to calculate fuzzy match ratio

    detection_threshold = 70

    set_ratios = process.extract(TextToCompare, datalist, scorer=fuzz.token_set_ratio)
    set_ratios_filtered = [i for i in set_ratios if i[1]> detection_threshold]
    
    sort_ratios = process.extract(TextToCompare, datalist, scorer=fuzz.token_sort_ratio)
    sort_ratios_filtered = [i for i in sort_ratios if i[1]> detection_threshold]
    
    partial_ratios = process.extract(TextToCompare, datalist, scorer=fuzz.partial_ratio)
    partial_ratios_filtered = [i for i in partial_ratios if i[1]> detection_threshold]

    ratios = process.extract(TextToCompare, datalist, scorer=fuzz.ratio)
    ratios_filtered = [i for i in ratios if i[1]> detection_threshold]

    wratios = process.extract(TextToCompare, datalist, scorer=fuzz.WRatio)
    wratios_filtered = [i for i in wratios if i[1]> detection_threshold]
             
    partial_token_set_ratios = process.extract(TextToCompare, datalist, scorer=fuzz.partial_token_set_ratio)
    partial_token_set_ratios_filtered = [i for i in partial_token_set_ratios if i[1]> detection_threshold]

    partial_token_sort_ratios = process.extract(TextToCompare, datalist, scorer=fuzz.partial_token_sort_ratio)
    partial_token_sort_ratios_filtered = [i for i in partial_token_sort_ratios if i[1]> detection_threshold]
    
    return jsonify({
        'set_ratios': SortArray(set_ratios_filtered),  
        'sort_ratios': SortArray(sort_ratios_filtered),
        'partial_ratios' : SortArray(partial_ratios_filtered),
        'ratios' : SortArray(ratios_filtered),
        'wratios': SortArray(wratios_filtered),
        'partial_token_set_ratios': SortArray(partial_token_set_ratios_filtered),
        'partial_token_sort_ratios': SortArray(partial_token_sort_ratios_filtered)
    })
  
def SortArray(array):
    dic = {}

    for item in array:
        name, score = item
        if dic.get(name, None) == None:
            dic[name] = score
        else:
            if score > dic[name]:
                dic[name] = score
            
    return dict(sorted(dic.items(), key=operator.itemgetter(1),reverse=True)) 



# driver function
# To stop server run in terminal > taskkill /f /im python.exe
if __name__ == '__main__':  
    app.run(host="localhost", port=8000, debug=False)








