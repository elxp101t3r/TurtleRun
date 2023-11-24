from turtle import Turtle, Screen
from random import randint
race_mode = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Bet!', prompt='which turtle is going to win this race?("red", "green", "orange" or "purple")')
colors = ["red", "green", "orange", "purple"]
y_pos = [-40, -20, 0, 20]
turtles = []

for i in range(len(colors)):
    n_turtle = Turtle(shape='turtle')
    n_turtle.penup()
    n_turtle.color(colors[i])
    n_turtle.goto(x=-230, y=y_pos[i])
    turtles.append(n_turtle)


if user_bet:
    race_mode = True

while race_mode:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.clear()
                print(f'You win! {winning_color} colored wins the race!')
            else:
                screen.clear()
                print(f'You lose.. {winning_color} colored wins the race.')
            race_mode = False
        r_distance = randint(0, 10)
        turtle.forward(r_distance)

screen.exitonclick()
