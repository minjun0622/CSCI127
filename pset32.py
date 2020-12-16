#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

first = input("Input file:")
second = input("Output file:")

air = pd.read_csv(first)

grouped_data = air.groupby("geo_entity_name").mean()["data_valuemessage"]
grouped_data.plot.bar()

plt.gcf().subplots_adjust(bottom=0.5)
fig = plt.gcf()
fig.savefig(second)
#plt.show()
