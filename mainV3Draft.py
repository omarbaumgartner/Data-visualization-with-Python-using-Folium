# IMPORTS
# Pour pouvoir utiliser le navigateur web
from branca.colormap import LinearColormap
import webbrowser
# Pour pouvoir lire les fichiers
import pandas as pd
# Pour les requetes GET SET ET DELETE
import requests
# pour les JSON
import json
from IPython.display import display
import folium
# Pour la légende
from folium import plugins
from folium import IFrame
# Pour les coordonnées du curseur
from folium.plugins import MousePosition
#from folium.plugins import HeatMap
# Searchbar
from folium.plugins import Search

# Filters
from folium.plugins import TimestampedGeoJson
# permettre d'importer les fichier excel
import csv
# Pour les légendes avec colormap - MatPlotLib
import branca.colormap as cm
# Mon fichier Py Methods
import methods


# DECLARATION  ---------
wildfireFile = pd.read_csv(
    '/home/omar/Desktop/PyPro/Data/7DayActiveFiresTo19-02-2020.csv')


json_result_string = wildfireFile.to_json(
    orient='records',
    double_precision=12,
    date_format='iso'
)
json_result = json.loads(json_result_string)
geojson = {
    'type': 'FeatureCollection',
    'features': []
}
for record in json_result:
    geojson['features'].append({
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [record['longitude'], record['latitude']],
        },
        'properties': record['acq_time'],
    })


# FOLIUM PART --------------------
RueDelaNat = [50.832367, 4.378715]
# Pour des raisons de performances
searchLimit = 5
# if too many marquers, use prefer_canvas to improve performance
m = folium.Map(location=RueDelaNat, zoom_start=2, min_zoom=2, max_zoom=8, control_scale=True,
               prefer_canvas=True, max_bounds=True)

#markerCluster = plugins.MarkerCluster()
marker_cluster = folium.plugins.MarkerCluster(name='site location').add_to(m)
for each in wildfireFile[0:searchLimit].iterrows():
   # add a marker for every record in the filtered data, use a clustered view
    tooltip = each[1]['confidence']
    marker = folium.Marker([each[1]['latitude'], each[1]['longitude']],
                           popup="Date : " +
                           str(each[1]['acq_date']) + "\nTime :\n" +
                           methods.timeFormat(
        each[1]['acq_time']),
        icon=folium.Icon(
        color='red', icon='glyphicon glyphicon-fire'),
        tooltip=tooltip)

    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'LineString',
                'coordinates': [each[1]['longitude'], each[1]['latitude']],
            },
            'properties': {
                'times': each[1]['acq_time'],
                'style': {
                    # 'color': line['color'],
                    # 'weight': line['weight'] if 'weight' in line else 5
                }
            }
        }
        for each in wildfireFile[0:searchLimit].iterrows()
    ]

    TimestampedGeoJson({
        'type': 'FeatureCollection',
        'features': features,
    }, period='PT1M', add_last_point=True).add_to(m)


# WEB BROWSER PART ------
# m.add_child(markerCluster)
MousePosition().add_to(m)
m.save('index.html')
url = 'index.html'
webbrowser.open(url, new=1)  # open in new tab
