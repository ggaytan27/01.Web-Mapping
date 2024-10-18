import folium

map = folium.Map(location=[31.697764200455353, -106.42825357685014], zoom_start=6)

fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[31.697764200455353, -106.42825357685014], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
print("Proceso Terminado")


