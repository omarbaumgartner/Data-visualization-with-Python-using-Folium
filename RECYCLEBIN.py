# RECYCLEBIN
'''
# print(df)
x = []
y = []
x = df.latitude.values
y = df.longitude.values
print("Length x : ", len(x))
print("Length y : ", len(y))
print("Latitude : \n", x)
print("Longitude : \n", y)
print(each[1]['latitude'], each[1]['longitude'])
index = 0
while(index < len(x)):
    print(x[index], y[index])
    folium.Marker([x[index], y[index]],
                   popup='<i>Mt. Hood Meadows</i>',
                   icon=folium.Icon(color='red', icon='info-sign'),
                   tooltip=tooltip).add_to(m)
     index += 5000
     print("Loading ", round((index/len(x))*100), "%")

'''
