import folium
import pandas

data = pandas.read_csv('files/Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
  if elevation < 1000:
    return 'green'
  elif elevation <= elevation < 3000:
    return 'orange'
  else:
    return 'red'

map = folium.Map(
    location=[29.130246, -110.965784], 
    zoom_start=6,
    tiles="OpenStreetMap",
    attr="Map data © OpenStreetMap contributors"
)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
  fg.add_child(folium.CircleMarker(
    location=[lt, ln],
    radius=6,
    popup=str(el)+' m', # el
    fill_color=color_producer(el), color = 'gray', fill_opacity=0.7
    ))
  
fg.add_child(folium.GeoJson(data=open('files/world.json', 'r', encoding='utf-8-sig'), 
                            style_function=lambda x: {'fillColor': 'yellow'}))

map.add_child(fg)

map.save("Map1.html")




"""
import folium
import pandas

data = pandas.read_csv('files/Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


map = folium.Map(
    location=[29.130246, -110.965784], 
    zoom_start=6,
    tiles="OpenStreetMap",
    attr="Map data © OpenStreetMap contributors"
)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
  fg.add_child(folium.Marker(
    location=[lt, ln],
    popup=str(el)+' m', # el
    icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
"""

"""
* STYLED
import folium
import pandas

data = pandas.read_csv('files/Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

html = '''<h4>Volcano information:</h4>
Height: %s m
'''

map = folium.Map(
    location=[29.130246, -110.965784], 
    zoom_start=6,
    tiles="OpenStreetMap",
    attr="Map data © OpenStreetMap contributors"
)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
  iframe = folium.IFrame(html=html % str(el), width=200, height=100)
  fg.add_child(folium.Marker(
    location=[lt, ln],
    popup=folium.Popup(iframe), # el
    icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
"""

"""
import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
 
html = '''
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
'''

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
map.add_child(fg)
map.save("Map_html_popup_advanced.html")
"""
