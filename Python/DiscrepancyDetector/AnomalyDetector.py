import pandas as pd
from tabulate import tabulate
import warnings
from sklearn.ensemble import IsolationForest
warnings.filterwarnings("ignore")

#Read Data from the input Excel and prepare Dataframe.
print ("Reading sample data from Excel...")
df = pd.read_excel('query_data.xlsx', sheet_name='Sheet1')

#function to detct anomaly in the data columns.
def DetectAnomaly(ColumnName, ExpectedContaminationPercent):

    print ("\nDetecting anomalies in " + ColumnName + " column:")

    model=IsolationForest(contamination=float(ExpectedContaminationPercent/100),max_features=1.0)
    model.fit(df[[ColumnName]])
    df['scores']=model.decision_function(df[[ColumnName]])
    df['anomaly']=model.predict(df[[ColumnName]])

    anomaly=df.loc[df['anomaly']==-1]
    anomaly_formatted = anomaly[['PatientID', ColumnName]]
    print(tabulate(anomaly_formatted, headers='keys', tablefmt='psql', showindex=False))

# invoke function to detect anomalies.
DetectAnomaly('Age', 5)
DetectAnomaly('BodyTemp', 5)