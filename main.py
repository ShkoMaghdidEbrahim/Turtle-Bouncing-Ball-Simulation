import turtle

X = 10
R = 2 / 3

screen = turtle.Screen()
canvas = screen.getcanvas()

turtle.title("Bouncing Ball")
turtle.showturtle()
turtle.setworldcoordinates(1.5, 0, 80, X)
turtle.speed(100)
turtle.color("green")
turtle.shape("circle")
turtle.turtlesize(0.7)

def up() :
    turtle.setheading(0)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(X * 2)

def down() :
    turtle.setheading(0)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(X * 2)

def right() :
    turtle.forward(320)
    turtle.left(90)
    turtle.forward(X / 10)

def left() :
    turtle.left(90)
    turtle.forward(320)
    turtle.right(90)
    turtle.forward(X / 10)
    turtle.right(90)

turtle.home()
for i in range(1, 7) :
    up()
    down()

turtle.home()
turtle.setheading(0)

for i in range(1, 7) :
    right()
    left()

turtle.goto(0, X)
turtle.width(2)
turtle.color("red")

for C in range(1, 20) :
    if C % 2 != 0 :
        turtle.shapesize(1, 1.3, 1)
        turtle.speed(2)
        turtle.goto(C * 5, 0)
    else :
        turtle.shapesize(1, 1, 1)
        turtle.speed(5)
        X = X * R
        turtle.goto(C * 5, X)
        turtle.write(('{:.2f}'.format(X) + "m"), font = ("Verdana", 10, "bold"))

turtle.mainloop()
