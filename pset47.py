#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(200):
  trey.forward(5)
  a = random.randrange(0,360,90)
  trey.right(a)
