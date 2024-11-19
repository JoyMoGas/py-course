import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')

map = folium.Map(
    location=[29.130246, -110.965784], 
    zoom_start=6,
    tiles="OpenStreetMap",
    attr="Map data © OpenStreetMap contributors"
)

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[29.13, -110.96],[28.13, -109.96]]:
  fg.add_child(folium.Marker(
    location=coordinates,
    popup="Hi a, a Marker",
    icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")