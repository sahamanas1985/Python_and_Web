import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.cluster import KMeans

# Load your dataset
df = pd.read_excel('covid_trainer_data.xlsx')

# Encode the labels
#label_encoder = LabelEncoder()
#df["result_encoded"] = label_encoder.fit_transform(df["Result_description"])


#scale the data
required_columns = ["Body_Temp","Cough_Severity","SPO2"]
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[required_columns]), columns=required_columns)

#print(df_scaled)


km = KMeans(n_clusters=8)
y_predicted = km.fit_predict(df_scaled)

df_scaled["cluster_predicted"] = y_predicted

print(df_scaled)

#plot 
'''

df0 = df_scaled[df_scaled["cluster_predicted"]==0]
df1 = df_scaled[df_scaled["cluster_predicted"]==1]
df2 = df_scaled[df_scaled["cluster_predicted"]==2]

plt.scatter(df0["Body_Temp"], df0["Cough_Severity"], color="green")
plt.scatter(df1["Body_Temp"], df1["Cough_Severity"], color="red")
plt.scatter(df2["Body_Temp"], df2["Cough_Severity"], color="blue")
plt.xlabel("Body_Temp")
plt.ylabel("Cough_Severity")
plt.legend()

plt.show()

'''

# elbow plot
'''
sse =[]
rng = range(1, 30)

for n in rng:
    km = KMeans(n_clusters=n)
    km.fit(df_scaled)
    sse.append(km.inertia_)

#print(sse)

plt.xlabel("k")
plt.ylabel("sum of sqr error")
plt.plot(rng, sse)
plt.show()

'''