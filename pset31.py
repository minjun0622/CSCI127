#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

first = input("Enter name of input file:")
second = input("Enter name of output file:")

homeless = pd.read_csv(first)
homeless["Fraction Single Women"] = homeless["Single Adult Women in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Single Women")

plt.show()
fig = plt.gcf()
fig.savefig(second)
    
