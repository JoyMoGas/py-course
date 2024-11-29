import folium
import pandas
import json

# Cargar datos de volcanes
data = pandas.read_csv('files/Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

# Función para asignar colores según la elevación
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Crear mapa
map = folium.Map(location=[29.130246, -110.965784], zoom_start=6, tiles="OpenStreetMap")

# Grupo de características
fgv = folium.FeatureGroup(name="Volcanoes")

# Agregar marcadores de volcanes
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln],
        radius=6,
        popup=str(el) + ' m',
        fill_color=color_producer(el),
        color='gray',
        fill_opacity=0.7
    ))

fgp = folium.FeatureGroup(name="Poulation")

# Cargar archivo GeoJSON
with open('files/world.json', 'r', encoding='utf-8-sig') as f:
    geojson_data = json.load(f)

# Función para estilo del GeoJSON basado en población
def style_function(feature):
    pop = feature['properties']['POP2005']
    if pop < 10000000:
        return {'fillColor': 'yellow'}
    elif 10000000 <= pop < 20000000:
        return {'fillColor': 'orange'}
    else:
        return {'fillColor': 'red'}

# Añadir GeoJSON al mapa
fgp.add_child(folium.GeoJson(data=geojson_data, style_function=style_function))



# Agregar el grupo al mapa
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# Guardar mapa
map.save("Map1.html")
