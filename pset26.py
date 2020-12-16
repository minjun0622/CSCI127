#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

boro1 = input("Enter first borough:")
boro2 = input("Enter second borough:")
filename = input("Enter file name:")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

pop['Fraction'] = ((pop[boro1] + pop[boro2]) / pop["Total"])

pop.plot(x="Year", y= 'Fraction')

fig = plt.gcf()
fig.savefig(filename)

