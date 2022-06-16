# 13'30''
# Ubacuje koordinate iz fajla volkanos sa id,ime itd i na kraju Lat i Lon
# u odvojenom novom pristupu u termu daje kod za citanje fajla volcanos a potom to ubacuje u cod kao i ja ovdje
# metod pretvaranja u listu i kombiniranja lon i lat lista sa zip
# na kraju reload koda i opere i markeri!!!

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
print(data)
print(type(data))
lat=list(data["LAT"])
lon=list(data["LON"])
print(len(lat),len(lon))


map = folium.Map(location=[38.58, -99.99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Moja Mapa")

for lt, ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Alo, ja sam marker!", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

