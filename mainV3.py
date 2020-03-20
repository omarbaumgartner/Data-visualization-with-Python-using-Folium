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

# permettre d'importer les fichier excel
import csv
# Pour les légendes avec colormap - MatPlotLib
import branca.colormap as cm
# Mon fichier Py Methods
import methods


# DECLARATION PART ---------
wildfireFile = pd.read_csv(
    '/home/omar/Desktop/PyPro/Data/7DayActiveFiresTo19-02-2020.csv')
# RECUPERATION DE DATASERT D'API -- Pas encore fonctionnel
# Declaration de l'API qu'on va rendre
url = "https://gis-gfw.wri.org/arcgis/rest/services/infrastructure/MapServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json"
# Requete GET et conversion en JSON
JSONContent = requests.get(url).json()
# Json Object to Json String
content = json.dumps(JSONContent, indent=4, sort_keys=True)

# FOLIUM PART --------------------
RueDelaNat = [50.832367, 4.378715]
# Pour des raisons de performances
searchLimit = 500
# if too many marquers, use prefer_canvas to improve performance
m = folium.Map(location=RueDelaNat, zoom_start=2, min_zoom=2, max_zoom=8, control_scale=True,
               prefer_canvas=True, max_bounds=True)

markerCluster = plugins.MarkerCluster()
#marker_cluster = folium.plugins.MarkerCluster(name='site location').add_to(m)
for each in wildfireFile[0:searchLimit].iterrows():
   # add a marker for every record in the filtered data, use a clustered view
    tooltip = each[1]['confidence']
    """marker = folium.Marker([each[1]['latitude'], each[1]['longitude']],
                           popup="Date : " +
                           str(each[1]['acq_date']) + "\nTime :\n" +
                           methods.timeFormat(
        each[1]['acq_time']),
        icon=folium.Icon(
        color='red', icon='glyphicon glyphicon-fire'),
        tooltip=tooltip) """

    markerCluster.add_child(folium.Marker([each[1]['latitude'], each[1]['longitude']],
                                          popup="Date : " +
                                          str(each[1]['acq_date']) + "\nTime :\n" +
                                          methods.timeFormat(
                                              each[1]['acq_time']),
                                          icon=folium.Icon(
        color='red', icon='glyphicon glyphicon-fire'),
        tooltip=tooltip))

''' folium.Marker([each[1]['latitude'], each[1]['longitude']],
                  popup="Date : " +
                  str(each[1]['acq_date']) + "\nTime :\n" +
                  methods.timeFormat(each[1]['acq_time']),
                  icon=folium.Icon(
        color='red', icon='glyphicon glyphicon-fire'),
        tooltip=tooltip).add_to(m) '''
'''     mc.add_child(folium.Marker([each[1]['latitude'], each[1]['longitude']],
                               popup="Date : " +
                               str(each[1]['acq_date']) + "\nTime :\n" +
                               methods.timeFormat(each[1]['acq_time']),
                               icon=folium.Icon(
        color='red', icon='glyphicon glyphicon-fire'),
        tooltip=tooltip).add_to(m)) '''


""" # Search bar
def style_one(x): return {'fillColor': 'green'}


geojson_layer = folium.GeoJson(wildfireFile['latitude'],
                               name='geojson') """

""" geojson_obj = folium.GeoJson(
    wildfireFile, style_function=style_one).add_to(marker_cluster) """

""" statesearch = Search(layer=marker_cluster,
                     geom_type='Point',
                     placeholder="Search",
                     collapsed=True,
                     search_label='name',
                     search_zoom=14,
                     position='topright'
                     ).add_to(m) """

# LEGEND PART
legend_html = '''
     # <div style =”position: fixed;
     bottom: 50px; left: 50px; width: 100px; height: 90px;
     border: 2px solid grey; z-index: 9999; font-size: 14px;
     “> & nbsp; Cool Legend < br >
     &nbsp; East & nbsp; < i class =”fa fa-map-marker fa-2x”
                  style =”color: green”> </i > <br >
     &nbsp; West & nbsp; < i class =”fa fa-map-marker fa-2x”
                  style =”color: red”> </i >
      </div>
     '''
# m.get_root().html.add_child(folium.Element(legend_html))


# colormap = cm.linearSet1.scale(0, 35).to_step(10)

''' color_map = LinearColormap(
    cmap, vmin=h2.frequencies.min(), vmax=h2.frequencies.max())
m.add_child(colormap) '''


''' text = 'your text here'

iframe = folium.IFrame(text, width=700, height=450)
popup = folium.Popup(iframe, max_width=3000)

l = folium.LayerControl().add_to(m) '''


# WEB BROWSER PART ------
# m.add_child(markerCluster)
MousePosition().add_to(m)
m.save('index.html')
url = 'index.html'
webbrowser.open(url, new=1)  # open in new tab
