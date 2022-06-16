# 1'53''
# za dobijanje kruznih markera umjesto Marker stavljamo CircleMarker sa jos nekim parametrima Circle-a kao radius, opacity (preklapanje  itd)
# i kad sam probao GRESKA: SyntaxError: keyword argument repeated # sa strelicom koja pokazuje na color. 
# Problem je rezultat moje ranije primjene njegovog naknadnog rjesenja koje se provlaci do ovog cod-a a koje on nije ovdje naknadno prilagodio
# rjesenje: doslovno prepisivanje ranijeg rjesenja i komanje koda s greskom
# BRAVO JA: Taman prije nego cu prepisati ponovo pogledam i uocim da ipak nisam na dobro mjesto stavio dodatne parametre. Premjestim ih i radi!!!
# Ipak, mjesavina radi ali prevladava boja naknadno dodana, brisem je...
# Na kraju morao prekucati sve s njegovim starim rjesenjem i dobio

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
    # fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(str(el)+"m", parse_html=True), icon=folium.Icon(color=color_producer(el))))
    # fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=folium.Popup(str(el)+" m", parse_html=True), icon=folium.Icon(color=color_producer(el), color = 'grey', fill_opacity=0.7)))
    # fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=folium.Popup(str(el)+"m", parse_html=True), icon=folium.Icon(color=color_producer(el)), color = 'grey', fill=True, fill_opacity=0.7))
    # fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=folium.Popup(str(el)+"m", parse_html=True), icon=folium.Icon(color=color_producer(el)), fill=True, fill_opacity=0.7))
    # fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=folium.Popup(str(el)+"m", parse_html=True), icon=folium.Icon(color=color_producer(el)), fill_opacity=0.7))
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m", fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))
    
map.add_child(fg)
map.save("Map1.html")

