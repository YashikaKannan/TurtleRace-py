from turtle import Turtle, Screen
import random

on = False
screen = Screen()
screen.setup(width=600, height=450)         # screen size
user = screen.textinput("Make your bet", "Enter your turtle color: ")       # to get a popup message

color = ["blue", "purple", "dark red", "magenta", "black"]
y_position = [-90, -50, -10, 30, 70]
turtles = []

for i in range(0, 5):
    tur = Turtle(shape="turtle")
    tur.color(color[i])
    tur.penup()
    tur.goto(x=-280, y=y_position[i])
    turtles.append(tur)

if user:
    on = True

while on:
    for turtle in turtles:
        if turtle.xcor() > 280:
            on = False
            winner = turtle.pencolor()
            if winner == user:
                print(f"You won the race!!\nThe {winner} turtle is the winner.")
            else:
                print(f"You lost the race!!\nThe {winner} turtle is the winner.")
        distance = random.randint(0, 12)
        turtle.forward(distance)

screen.exitonclick()
