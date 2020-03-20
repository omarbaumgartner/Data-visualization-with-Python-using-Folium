import csv


class toMap:


def setMap(self):
    # --- Save Countries, Latitudes and Longitudes ---
    filename = 'log.csv'
    pais, lats, lons = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)

        next(reader)

        for row in reader:
            pais.append(str(row[0]))
            lats.append(float(row[1]))
            lons.append(float(row[2]))

    # count the number of times a country is in the list
    unique_pais = set(pais)
    unique_pais = list(unique_pais)

    c_numero = []

    for p in unique_pais:
        c_numero.append(pais.count(p))
        print p, pais.count(p)

    maximo = max(c_numero)

    # --- Build Map ---
    import cartopy.crs as ccrs
    import cartopy.io.shapereader as shpreader
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np

    cmap = mpl.cm.Blues

    # --- Using the shapereader ---
    test = 0
    shapename = 'admin_0_countries'
    countries_shp = shpreader.natural_earth(resolution='110m',
                                            category='cultural', name=shapename)

    ax = plt.axes(projection=ccrs.Robinson())
    for country in shpreader.Reader(countries_shp).records():
        nome = country.attributes['name_long']
        if nome in unique_pais:
            i = unique_pais.index(nome)
            numero = c_numero[i]
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                              facecolor=cmap(numero / float(maximo), 1),
                              label=nome)
            test = test + 1

        else:
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                              facecolor='#FAFAFA',
                              label=nome)

    if test != len(unique_pais):
        print "check the way you are writting your country names!"

    plt.show()


def main():
    m = toMap()
    m.setMap()
