# IMPORTS
# Navigateur web
import webbrowser
# Lecture de fichiers
import pandas as pd
import csv
import json
import folium
from folium import plugins
from folium.plugins import MousePosition
from folium.plugins import TimestampedGeoJson
# Mes méthodes
import methods

# DECLARATION  -------------
wildfireFile = pd.read_csv(
    '/home/omar/Desktop/PyPro/Data/7DayActiveFiresTo19-02-2020.csv')
# Centrer map sur :
RueDelaNat = [50.832367, 4.378715]
# Pour des raisons de performances, limite de recherche
searchLimit = 5000


# FOLIUM PART --------------------

# if too many marquers, use prefer_canvas to improve performance
m = folium.Map(location=RueDelaNat, zoom_start=2, min_zoom=2, max_zoom=10, control_scale=True,
               prefer_canvas=True, max_bounds=True)

markerCluster = plugins.MarkerCluster(name="Wildfires")
for each in wildfireFile[0:searchLimit].iterrows():
    tooltip = each[1]['confidence']
    markerCluster.add_child(folium.Marker([each[1]['latitude'], each[1]['longitude']],
                                          popup="Date : " +
                                          str(each[1]['acq_date']) + "\nTime :\n" +
                                          methods.timeFormat(
                                              each[1]['acq_time']),
                                          icon=folium.Icon(
        color='red', icon='glyphicon glyphicon-fire'),
        tooltip=tooltip))


# WEB BROWSER PART ------
markerCluster.add_to(m)
folium.TileLayer(tiles='Stamen Toner', name="Stamen Toner").add_to(m)
folium.TileLayer(tiles='Stamen Terrain', name="Stamen Terrain").add_to(m)
folium.LayerControl(collapsed=True).add_to(m)
MousePosition().add_to(m)
m.save('index.html')
url = 'index.html'
webbrowser.open(url, new=1)  # open in new tab
