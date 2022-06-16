# 7'55''
# Kao sto naslov sugerira, bavimo se bojom markera kako bi ista njome signalizirala visinsku kategoriju
# To s folium-om ne mozemo direktno nego ubacujuci funkciju "color_producer" ispred  i return-ajuci 'red'. 
# Kad je pokazao da stavljajuci u icon=folium... izraz tako formiranu funkciju koja ondas na to mjesto returna return, ide na usloznjavanje logike funkcije kako bi ona razlikovala visine iz csv-ea i prema tome mjenjala return-boju
# U def-parametar stavlja "elevation" a u call-argument "el" te gradi logiku u funsu sa parametrom elevation. Nije mi jasno odkud povlaci vrijednosti za elevation
# Nakon malo razmisljanja skuzio sam: elevation je proizvoljan naziv kojim se razvija logika. Pri pozivanju funs-a na mjesto tog naziva stupa el-realna i promjenjiva varijabla koja sad odigrava prema def-logici!!!
# Izvodi kod i markeri se bojaju razlicito!!!


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
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(str(el)+"m", parse_html=True), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("Map1.html")

