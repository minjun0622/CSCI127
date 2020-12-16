#Minjun Seo
#minjun.seo58@myhunter.cuny.edu

import turtle
wn = turtle.Screen()

x = input("Enter hexcode color:")
x = "#" + x

alex = turtle.Turtle()
alex.shape("turtle")
alex.color(x)
alex.stamp()

wn.exitonclick()

