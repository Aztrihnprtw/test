import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("I LOVE YOU 🌸")
screen.setup(900, 800)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

t.color("#ff69b4")

# Membuat bentuk bunga
for i in range(120):
    angle = 2 * math.pi * i / 120

    # Bentuk bunga dengan 6 kelopak
    r = 250 * abs(math.sin(3 * angle))

    x = r * math.cos(angle)
    y = r * math.sin(angle)

    t.goto(x, y)

    t.write(
        "I LOVE YOU",
        align="center",
        font=("Arial", 10, "bold")
    )

turtle.done()