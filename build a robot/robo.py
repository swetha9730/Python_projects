#importing module
import turtle as t

#defining a function to draw rectangles
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

#setting the background
t.penup()
t.speed('slow')
t.bgcolor('white')

#making the robot using the previously defined rectangles
# feet
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# legs
t.goto(-25, -50)
rectangle(15, 100, 'light blue')
t.goto(-55, -50)
rectangle(-15, 100, 'light blue')

# body
t.goto(-90, 100)
rectangle(100, 150, 'red')

# arms
t.goto(-150, 70)
rectangle(60, 15, 'light blue')
t.goto(-150, 110)
rectangle(15, 40, 'light blue')
t.goto(10, 70)
rectangle(60, 15, 'light blue')
t.goto(55, 110)
rectangle(15, 40, 'light blue')

# neck
t.goto(-50, 120)
rectangle(15, 20, 'light blue')

# head
t.goto(-85, 170)
rectangle(80, 50, 'red')

# eyes
t.goto(-60, 160)
rectangle(30, 15, 'light blue')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')