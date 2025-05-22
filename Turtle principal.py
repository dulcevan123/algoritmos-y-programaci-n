
Import turtle

screen = turtle.Screen()
screen.bgcolor("black")

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.left(72)

def draw_decorative_border():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("white")
    pen.pensize(3)
    corners = [(-400, 250), (400, 250), (400, -250), (-400, -250)]
    pentagon_size = 50

    for corner in corners:
        pen.penup()
        pen.goto(corner)
        pen.pendown()
        draw_pentagon(pen, pentagon_size)

    pen.penup()
    pen.goto(-400, 200)
    pen.pendown()
    pen.forward(800)

    pen.penup()
    pen.goto(-400, -200)
    pen.pendown()
    pen.forward(800)

    pen.penup()
    pen.goto(-200, 250)
    pen.pendown()
    pen.setheading(270)
    pen.forward(500)

    pen.penup()
    pen.goto(200, 250)
    pen.pendown()
    pen.setheading(270)
    pen.forward(500)

def write_name():
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.speed(0)
    writer.penup()

    name = "VANESSA"
    colors = ["white", "gray10"] #
    x_start = -250

    for index, letter in enumerate(name):
        writer.goto(x_start + index * 70, -50)
        writer.color(colors[index % 2])
        writer.write(letter, font=("Arial", 48, "bold"))

draw_decorative_border()
write_name()

turtle.done()
