import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print ("Reading training data from Excel")
df = pd.read_excel(r"flat_prices.xlsx")
#print (df)

# Get Dummies (Numerize the text column into seperate columns with 0 and 1)
citydummy = pd.get_dummies(df.City)
#print (citydummy)

#merge dummy with main dataframe.
merged = pd.concat([df, citydummy], axis='columns')
#print (merged)

# remove the original City column and One of the dummy columns (Dummy variable trap) 
# because double 0 in other 2 columns means it must be 1 for this column.

#final = merged.drop(['City', 'Mumbai'], axis='columns')
final = merged.drop(['City'], axis='columns')
#print (final)

# create linear regression model
model = LinearRegression()

# X is feature columns - convert to numpy array, 
# y is result
X = final.drop(['Price'], axis='columns').to_numpy()
y = final.Price

#print (X)
#print (y)

model.fit(X, y)

# Predict 1348 sqft flat price in Kolkata
pred = model.predict([[1348, 0, 1, 0]])
print (pred)

score = model.score(X, y)
print (score)

# show plot

plt.xlabel('Sqft')
plt.ylabel('Price')
plt.scatter(df.Sqft, df.Price, color='red', marker = '+')
plt.show()

