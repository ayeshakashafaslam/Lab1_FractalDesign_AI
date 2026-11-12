# Design Lab 01 - Fractal Tree
# Name: <YOUR NAME>
# Reg No: <YOUR REG NO>

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def draw_tree(length, depth):
    # base case: stop when depth reaches 0
    if depth == 0:
        return

    # thick brown trunk, thin green leaves
    t.pensize(depth)
    if depth > 3:
        t.color("sienna")
    else:
        t.color("lime green")

    t.forward(length)

    # left branch
    t.left(25)
    draw_tree(length * 0.75, depth - 1)

    # right branch
    t.right(50)
    draw_tree(length * 0.75, depth - 1)

    # go back to the start of this branch
    t.left(25)
    t.penup()
    t.backward(length)
    t.pendown()


# move to the bottom of the screen and face up
t.penup()
t.goto(0, -250)
t.left(90)
t.pendown()

draw_tree(80, 9)

screen.mainloop()