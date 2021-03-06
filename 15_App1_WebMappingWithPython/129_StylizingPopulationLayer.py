# 9'35''
# promjena boja zemalja prema br. stanovnika
# dodatna logika koristi dict-comprehension w/ cond.logic unutar koje prvi put susrecem više if i više else!!!

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <=elevation <3000:
        return 'orange'
    return 'red'

map = folium.Map(location=[38.58, -99.99], zoom_start=3, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Moja Mapa")

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m", fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))
    
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))


map.add_child(fg)
map.save("Map1.html")

