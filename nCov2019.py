import csv
import pandas as pd


confirmed_path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/time_series/time_series_2019-ncov-Confirmed.csv'

confirmed_df = pd.read_csv(confirmed_path)
confirmed_df['total'] = confirmed_df.iloc[:, -1] #.sum(axis=1)

confirmed_summary = confirmed_df[['Lat', 'Long', 'total']]
confirmed_summary.to_json('confirmed.json',orient='records')
