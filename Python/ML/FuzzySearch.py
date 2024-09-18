from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import numpy as np

dataframecolumn = pd.DataFrame(['Apple Inc', 'Facebook', 'Alphabet Inc', 'Pricewaterhouse Coopers', 'Samsung electronics', 
'Samsung Semiconductors', 'Tata motors', 'Toyota Motors', 'Tata Consultancy services', 'Audi', 'Adobe', 
'Microsoft', 'Oneplus', 'Oneweb', 'Airtel', 'Intel', 'IBM', 'BMW', 'Emirates', 'Ericsson'])
dataframecolumn.columns = ['Match']

#print(dataframecolumn)

compare = pd.DataFrame(['tatacon'])
compare.columns = ['compare']


#print(compare)

dataframecolumn['Key'] = 1
compare['Key'] = 1
combined_dataframe = dataframecolumn.merge(compare,on="Key",how="left")
combined_dataframe = combined_dataframe[~(combined_dataframe.Match==combined_dataframe.compare)]

def partial_match(x,y):
    return(fuzz.WRatio(x,y))
partial_match_vector = np.vectorize(partial_match)

combined_dataframe['score']=partial_match_vector(combined_dataframe['Match'],combined_dataframe['compare'])
combined_dataframe = combined_dataframe[combined_dataframe.score>=50]

print(combined_dataframe)