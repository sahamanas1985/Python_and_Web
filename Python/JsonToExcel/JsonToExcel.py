import pandas as pd
import json
 
# Load your JSON data
with open('input.json', encoding='utf-8') as json_file:
    data = json.load(json_file, )
 
# Use json_normalize to flatten the nested JSON into a flat table
df = pd.json_normalize(data)
 
# Convert the flat table to an Excel file
df.to_excel('output.xlsx', index=False)