#CSci 127 Teaching Staff
#September 2020
#A template for a program that draws nested squares 
#Modified by: Minjun Seo
#Email: minjun.seo58@myhunter.cuny.edu

import turtle
def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist, 
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def squares(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 4 times:  moves forward that length, turns 90 degrees, 
    and calls squares(t, length/2).
    """
    if (length > 10):
        for i in range(4):
            t.forward(length)
            t.left(90)
        squares(t, length/2)
    
     


def nestedSquares(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 4 times:  moves forward that length, turns 90 degrees, 
    and calls nestedSquares(t, length/2).
    """
    if (length > 10):
        for i in range(4):
            t.forward(length)
            t.left(90)
            nestedSquares(t, length/2)


def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    squares(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedSquares(tess, n)

if __name__ == "__main__":
     main()
     
