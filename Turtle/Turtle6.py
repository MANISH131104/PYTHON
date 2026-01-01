import turtle
t = turtle.Turtle()

turtle.shape("turtle")
# turtle.pencolor("red")
# turtle.fillcolor("green")
turtle.color("red","blue")

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()

turtle.pensize(10)
turtle.color("red","orange")

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

print(turtle.pos())

turtle.goto(-100,-100)




turtle.done()
