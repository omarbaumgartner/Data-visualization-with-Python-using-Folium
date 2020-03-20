import webbrowser
import matplotlib.pyplot as plt
import cartopy.crs as ccrs                   # import projections
import cartopy.feature as cf                 # import features
import pandas as pd
import requests
import json
import folium
from IPython.display import display
from folium.plugins import HeatMap
import csv


# DECLARATION PART ---------
x = []
y = []
df = pd.read_csv(
    '/home/omar/Desktop/Python Project/7DayActiveFiresTo19-02-2020.csv')
# print(df)
x = df.latitude.values
y = df.longitude.values
# print("Latitude : \n", x)
# print("Longitude : \n", y)


""" df = pd.read_excel(
    r'/home/omar/Desktop/Python Project/7DayActiveFiresTo19-02-2020.csv')
print(df) """
# declaration de l'API qu'on va rendre
url = "https://gis-gfw.wri.org/arcgis/rest/services/infrastructure/MapServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json"
# requete get + conversion en json
JSONContent = requests.get(url).json()
# Json Object to Json String
content = json.dumps(JSONContent, indent=4, sort_keys=True)


# MATPLOTLIB PART -------------------
# create a set of axes with Mercator projection
ax = plt.axes(projection=ccrs.Mercator())
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.LAND)
ax.set_title("Worldwide Bushfires")
plt.show()


# FOLIUM PART --------------------

# print(content)
m = folium.Map()
tooltip = 'Click me!'
index = 0
print("Length x : ", len(x))
print("Length y : ", len(y))
print(x[392308])
while(index < len(x)):
    # print(x[index], y[index])
    folium.Marker([x[index], y[index]],
                  popup='<i>Mt. Hood Meadows</i>',
                  icon=folium.Icon(color='red', icon='info-sign'),
                  tooltip=tooltip).add_to(m)
    print("Loading ", index)
    index += 1000
''' 
folium.Marker([45.3288, -121.6625],
              popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(m) '''
m.save('index.html')
# WEB BROWSER PART ------
url = 'index.html'
webbrowser.open(url, new=2)  # open in new tab
