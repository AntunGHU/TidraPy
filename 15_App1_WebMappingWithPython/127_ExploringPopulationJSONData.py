# 5'34''
# Dodavacemo jos jedan layer (poligon-layer) postojecim 2 leyerima(base map i layer circl-ova)
# kao izvor informacija ovom layeru bit ce fajl "world.json" koji je GeoJason - malo specifican
# Pola videa pokazuje sta sve ima u json-fajlu: sve zemlje, vrlo velik
# i dodaje liniju koda L30


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
    
fg.add_child(folium.GeoJson())

map.add_child(fg)
map.save("Map1.html")

