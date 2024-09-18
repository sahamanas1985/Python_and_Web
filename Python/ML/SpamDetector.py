import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('spam.csv')

# encode ham and spam with numbers
df['spam'] = df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df_final = df.drop(['Category'], axis='columns')

# Vectorize the text content
v = CountVectorizer()
VectorizedMessage = v.fit_transform(df_final['Message'])

#train model
model = MultinomialNB()
model.fit(VectorizedMessage, df_final['spam'])

#use model to detect spam
emails = [
    "Can you ask him out on monday",
    "Congratulations, you have won a prize"
]

VectorizedEmails = v.transform(emails)
output = model.predict(VectorizedEmails)

print(output)