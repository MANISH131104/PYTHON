import turtle

# creating turtle object
t = turtle.Turtle()
turtle.speed(3)
turtle.pencolor("blue")

# taking input for sides of polygon
n= int(input("Enter sides of polygon :"))

# length of each sides of polygon
length= 100

# angle for regular polygon
angle = 360/n

# draw polygon
for i in range(n):
    turtle.forward(length)
    turtle.right(angle)


turtle.done()
