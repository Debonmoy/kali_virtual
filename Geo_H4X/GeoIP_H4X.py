import geocoder, folium

target_ip=str(input('[*] Enter target ip: '))
ip=geocoder.ip(target_ip)
address=ip.latlng
mymap=folium.Map(location=address, zoom_start=12)
folium.Circle(address, radius=500).add_to(mymap)
mymap.save("mymap.html")
