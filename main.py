# (sqrt(cos(x))*cos(400*x)+sqrt(abs(x))-0.4)*(4-x*x)^0.1
import math
import turtle

# Define the function
def f(x):
    return (math.sqrt(abs(math.cos(x))) * math.cos(400 * x) + math.sqrt(abs(x)) - 0.4) * (4 - x**2)**0.1

# Set up the turtle screen
screen = turtle.Screen()
screen.setworldcoordinates(-2, -2, 2, 2)
screen.bgcolor("black")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()

# Draw the x and y
t.pencolor("white")

t.penup()
t.goto(-2, 0)
t.pendown()
t.goto(2, 0)

t.penup()
t.goto(0, -2)
t.pendown()
t.goto(0, 2)

# Draw the function
t.penup()
x = -1.567
step = 0.001

t.pencolor("red")
# Move to the starting point
try:
    t.goto(x, f(x))
    t.pendown()
except:
    pass

while x <= 1.567:
    try:
        t.goto(x, f(x))
    except:
        t.penup()
        try:
            t.goto(x + step, f(x + step))
            t.pendown()
        except:
            pass
    x += step
    # try
    print(x,step)

# Wait for the user to close the window
turtle.done()
