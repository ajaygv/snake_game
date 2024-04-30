#turtle race 
from turtle import Turtle,Screen
import random
color=["red","blue","green","black","grey"]
a=Turtle()
b=Turtle()
c=Turtle()
d=Turtle()
a.shape("turtle")
a.color(random.choice(color))
b.shape("turtle")
b.color(random.choice(color))
c.shape("turtle")
c.color(random.choice(color))
d.shape("turtle")
d.color(random.choice(color))




screen=Screen()
screen.setup(width=500,height=500)
user_bet=screen.textinput(title="MAKE your bet",prompt="which turtle will win")
a.penup()
a.goto(x=-200,y=-200)
b.penup()
b.goto(x=-200,y=-100)
c.penup()
c.goto(x=-200,y=100)
d.penup()
d.goto(x=-200,y=200)





print(user_bet)
screen.exitonclick()

