# Samo je u 4 min najavio koristenje for-loopa za ubacivanje mnogo novih markera koristenjem podataka iz csv-fajla

import folium
map = folium.Map(location=[45.81643989741451, 15.923494193695529], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Moja Mapa")
for coordinates in [[45.91, 15.82], [45.81, 15.92]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Alo, ja sam marker!", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

