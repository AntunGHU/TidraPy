# 3'20''
# Dodaje u novu liniju koda L31

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

map = folium.Map(location=[38.58, -99.99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Moja Mapa")

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m", fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))
    
fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
#! pri dodavanju encoding... iskace upozorenje na videu o promjenama u novijim verzijama folium-a:
#? Note:The recent version of Folium needs a string instead of a file as data input. Therefor you may need to add a read() method:
#! i dodaje ga u nastavku videa! Nakon toga izvrsava i dobija novi layer! Dobijam i JA!!! Glavna odlika dodatka je u podebljalim granicama drzava!

map.add_child(fg)
map.save("Map1.html")

