#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu
#Date: September 3, 2020

import turtle

wn = turtle.Screen()
wn.bgcolor("hotpink")

alex = turtle.Turtle()
alex.shape("turtle")
alex.fillcolor("yellow")
alex.pencolor("red")
alex.shape("turtle")

for i in range(36):
    alex.forward(200)
    alex.right(170)
    alex.stamp()

wn.exitonclick()
