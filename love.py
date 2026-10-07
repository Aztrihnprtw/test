import turtle
import math

# Layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("I LOVE YOU ❤️")
screen.setup(900, 700)

# Turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Warna tulisan
t.color("#ff69b4")

# Persamaan bentuk hati
# x = 16 sin³(t)
# y = 13 cos(t) - 5 cos(2t) - 2 cos(3t) - cos(4t)

for i in range(120):
    angle = 2 * math.pi * i / 120

    x = 16 * math.sin(angle) ** 3
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    # Perbesar bentuk hati
    x *= 25
    y *= 25

    t.goto(x, y)

    # Tulisan berulang
    t.write(
        "I LOVE YOU",
        align="center",
        font=("Arial", 10, "bold")
    )

turtle.done()