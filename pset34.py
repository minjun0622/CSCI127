#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

first = input("Enter input file:")
second = input("Enter output file:")

df = pd.read_csv(first)
df["Date"] = pd.to_datetime(df["Date"].apply(str))

df["% Attending"] = (df["Present"]/df["Enrolled"]) * 100
graph = df.plot(x = "Date", y = "% Attending")

fig = plt.gcf()
fig.savefig(second)
plt.show()



