#Name: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import turtle

x = int(input("Number of stamps:"))

alex = turtle.Turtle()
alex.shape("circle")
alex.penup()

steps = 20

for i in range(x):
    alex.stamp()
    if (i % 4 == 0):
        steps += 2

    alex.forward(steps)
    alex.right(24)

    
        

        

