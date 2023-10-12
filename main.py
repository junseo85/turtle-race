import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
tim = Turtle(shape="turtle")
tim.penup()
tim.color(user_bet)
tim.goto(x=-230, y=-120)
all_turtles.append(tim)
x = -230
y = -120
def computer(computer_color):
    global y
    computer =Turtle(shape="turtle")
    computer.penup()
    computer.color(computer_color)
    y += 50
    computer.goto(x, y)
    all_turtles.append(computer)
# def create_opponent():
#     for color in colors:
#         tim.color(color)
# for user in range(6):
#     tim = Turtle(shape="turtle")
#     create_opponent()
#     tim.penup()
#     y += 20
#     tim.goto(x, y)

for color in colors:
    if color != user_bet:
        computer(color)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() >230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtles.forward(rand_distance)
screen.exitonclick()