import re
import pandas as pd
from datetime import datetime
def preprocess(data):
    pattern = r'\[(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}:\d{2}\s?[APM]{2})\] (.*?): (.*)'
    matches = re.findall(pattern, data)[1:]
    df = pd.DataFrame(matches, columns=['Date', 'Time', 'Sender', 'Message'])
    df['DateTime'] = df.apply(lambda row: datetime.strptime(f"{row['Date']} {row['Time']}", '%d/%m/%y %I:%M:%S %p'), axis=1)
    df['Day'] = df['DateTime'].dt.day
    df['Month'] = df['DateTime'].dt.month
    df['Year'] = df['DateTime'].dt.year
    df['Hour']=df['DateTime'].dt.hour
    df['Minute']=df['DateTime'].dt.minute
    df = df.drop(columns=['Date', 'Time'])
    return df
 