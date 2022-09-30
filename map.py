import folium
import pandas

def colordisp(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name=list(data["NAME"])
map=folium.Map(location=[40.58,-99.09],zoom_start=6)
fgv=folium.FeatureGroup(name="Volcano Map")
fgp=folium.FeatureGroup(name="Population Map")
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
for lt,ln,el,nam in zip(lat,lon,elev,name):
    iframe=folium.IFrame(html=html%(nam,nam,el),width=200,height=100)
    fgv.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=colordisp(el))))

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'green' 
                                                     if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")

