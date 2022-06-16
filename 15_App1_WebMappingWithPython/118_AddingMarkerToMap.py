# lekcija dodavanja tocki prethodno napravljenoj mapi (iz openStreet-a i folium-a)"
# lekcija u kojoj prelazimo na .py fajl, kod njega Map1.py ali ja cu uklopiti u projek Tidra i pojedine lekcije. Nadam se da ce git moci sve pratiti.
# K-de i terma prebacujem u py-fajl pa map k-di dodajem novi parametar
# Potom izvodim k-de - Map1.html se reloada sa novim param
# Pregledam u Operi

import folium
map=folium.Map(location=[45.81643989741451, 15.923494193695529], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Moja Mapa")
fg.add_child(folium.Marker(location=[45.5, 15.5], popup="Alo, ja sam marker!", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")

# sad kad smo reloadali idemo dodavati markere, Ar gleda dir(folium) a potom i help(Marker) kako bi pokazao da treba citati helpove. Ubacuje izmedju L2 i L3 kod za marker ireloada Opera
# na zalost kod njega ima a kod mene nema markera