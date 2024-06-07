
# Python program to draw smile 
# face emoji using turtle
import turtle
 
# turtle object
pen = turtle.Turtle()
 
# function for creation of eye
def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()
 
 
# draw face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()
 
# draw eyes
pen.goto(-35, 120)
eye('black', 15)
pen.goto(35, 120)
eye('black', 15)

# draw mouth
pen.goto(-45, 80)
pen.down()
pen.right(90)
pen.circle(45, 180)
pen.up()

pen.end_fill()
pen.hideturtle()
turtle.done()