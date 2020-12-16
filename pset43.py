#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import folium
import pandas as pd

fileName = input("Enter file name: ")
output = input("Enter output file name: ")

df = pd.read_csv(fileName)
mapNYC = folium.Map(location=[40.768731, -73.964915])

for index,row in df.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)

mapNYC.save(output)
