import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('iris.csv')

km = KMeans(n_clusters=3)
y_pred = km.fit_predict(df[['PetalLengthCm', 'PetalWidthCm']])
df['Cluster'] = y_pred

df1 = df[df.Cluster == 0]
df2 = df[df.Cluster == 1]
df3 = df[df.Cluster == 2]

#df1 = df[df.Species == 'Iris-setosa']
#df2 = df[df.Species == 'Iris-versicolor']
#df3 = df[df.Species == 'Iris-virginica']


#plt.scatter(df1.PetalLengthCm, df1.PetalWidthCm, color='red', marker = '*')
#plt.scatter(df2.PetalLengthCm, df2.PetalWidthCm, color='green', marker = '*')
#plt.scatter(df3.PetalLengthCm, df3.PetalWidthCm, color='blue', marker = '*')
#plt.show()

#find optimum value of K from Elbow chart

k_range = range(1, 10)
sse = []
for k in k_range:
    km = KMeans(n_clusters=k)
    km.fit(df[['PetalLengthCm', 'PetalWidthCm']])
    sse.append(km.inertia_)

plt.xlabel = 'K'
plt.ylabel = 'Sum of squared error'
plt.plot(k_range, sse)
plt.show()
