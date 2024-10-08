from turtle import Turtle,Screen
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which Turtle will win the race? Enter your color: ")

colors = ["red", "blue", "green", "yellow", "purple","black","pink"]
y_positions = [-100, -60, -20, 20, 60, 95, 120]  # Y-positions to line up the turtles
all_turtles=  []

# Create five turtles of different colors and place them at different starting positions
for turtle_index in range(7):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)
if user_bet:
    race_on=True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won , the winner is {user_bet}")
            else:
                print(f"You lost the winner is {winner}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()

