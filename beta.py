import pandas as pd
import csv
import methods
from geojson import Feature, Point

wildfireFile = pd.read_csv(
    '/home/omar/Desktop/PyPro/Data/7DayActiveFiresTo19-02-2020.csv')

features = []

for each in wildfireFile[0:10].iterrows():
    time = methods.timeFormat(each[1]['acq_time'])
    point = {
        "type": "Feature",
        "geometry":
            {
                "type": "Point",
                "coordinates": [each[1]['latitude'], each[1]['longitude']],
            },
        "properties":
            {
                "confidence": each[1]['confidence'],
                "date": each[1]['acq_date'],
                "time": time,
            },
    }
    features.append(point)

print(features)
