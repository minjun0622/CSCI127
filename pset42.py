#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import folium

mapNYC = folium.Map(location=[40.75,-74.125],zoom_start=10)
folium.Marker(location = [40.768731, -73.964915], popyp = "Hunter College").add_to(mapNYC)

mapNYC.save(outfile = 'nycMap.html')
