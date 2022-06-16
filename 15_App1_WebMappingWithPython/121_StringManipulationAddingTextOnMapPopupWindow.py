# 5'08''
# dodaje Elev list kao izvor inf za svaki marker popup jednostavnim dodavanjem u for, zip itd
# u videu na 3'51'' upozorenje o utjecaju ' quota. Da se to ne desi treba napisati za el u popup-u
#? popup=folium.Popup(str(el), parse_html=True)

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])



map = folium.Map(location=[38.58, -99.99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Moja Mapa")

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(str(el)+"m", parse_html=True), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

