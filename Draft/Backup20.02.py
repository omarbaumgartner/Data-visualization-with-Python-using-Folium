import matplotlib.pyplot as plt
import cartopy.crs as ccrs                   # import projections
import cartopy.feature as cf                 # import features
import pandas as pd
import requests
import json
import folium
from IPython.display import display
from folium.plugins import HeatMap

# create a set of axes with Mercator projection
ax = plt.axes(projection=ccrs.Mercator())
ax.add_feature(cf.COASTLINE)                 # plot some data on them
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.LAND)
ax.set_title("Worldwide Bushfires")                        # label it

df = pd.read_excel(r'/home/omar/Desktop/Python Project/data.xls')
# print(df)

""" ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

plt.text(ny_lon - 3, ny_lat - 12, 'New York',
         horizontalalignment='right', color="red",
         transform=ccrs.Geodetic()) """

# declaration de l'API qu'on va rendre
url = "https://gis-gfw.wri.org/arcgis/rest/services/infrastructure/MapServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json"
# requete get + conversion en json
JSONContent = requests.get(url).json()
# Json Object to Json String
content = json.dumps(JSONContent, indent=4, sort_keys=True)
# print(content)
m = folium.Map()

m.render()
plt.show()
