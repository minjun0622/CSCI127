#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

fileName = input("Enter file name:")

df = pd.read_csv(fileName)

tick = len(df)
print("There were", tick, " film permits.")

boroPermits = df["Borough"].value_counts()
print(boroPermits)


popEvents = df["EventType"].value_counts()[:3]
print("The three most popular type of events were:")
print(popEvents)
               





