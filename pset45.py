#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import folium
import pandas as pd

csvfile = input("Enter input file: ")
output = input("Enter output file: ")
boro = input("Enter name of boro: ")

df = pd.read_csv(csvfile)
dfCopy = df.groupby("Borough").get_group(boro)

mapNYC = folium.Map(location=[40.768731, -73.964915])

for index,row in dfCopy.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Address"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)

mapNYC.save(output)
