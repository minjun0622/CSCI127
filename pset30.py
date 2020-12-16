#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import pandas as pd

filename = input("Insert file name:")
average = input("Choose one to average:")

stars = pd.read_csv(filename)

aggregate = stars.groupby('Star type').mean()

print(aggregate[average])
    
