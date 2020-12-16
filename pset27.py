#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough = input("Enter borough:")

print("Min", pop[borough].min())
print("Max", pop[borough].max())
print("Mean", pop[borough].mean())
print("Median", pop[borough].median())
print("Standard deviation", pop[borough].std())
