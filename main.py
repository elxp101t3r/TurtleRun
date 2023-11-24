from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Bet!', prompt='which turtle is going to win this race?("red", "green", "orange" or "purple")')
colors = ["red", "green", "orange", "purple"]
turtles = []
for i in range(len(colors)):
    turtles.append(Turtle(shape='turtle'))
for i in range(len(turtles)):
    if i == 0:
        t1 = turtles[i]
    elif i == 1:
        t2 = turtles[i]
    elif i == 2:
        t3 = turtles[i]
    elif i == 3:
        t4 = turtles[i]

c1 = choice(colors)
colors.remove(c1)
c2 = choice(colors)
colors.remove(c2)
c3 = choice(colors)
colors.remove(c3)
c4 = choice(colors)
colors.remove(c4)
t1.color(c1)
t1.penup()
t1.goto(x=-225, y=-100)
t2.color(c2)
t2.penup()
t2.goto(x=-225, y=-50)
t3.color(c3)
t3.penup()
t3.goto(x=-225, y=0)
t4.color(c4)
t4.penup()
t4.goto(x=-225, y=50)

screen.exitonclick()
