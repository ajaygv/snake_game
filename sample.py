from turtle import Turtle 
import random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        random_xpoint=random.randint(200,200)
        random_ypoint=random.randint(200,200)
        self.goto(random_xpoint,random_ypoint)

    def refesh(self):
        random_xpoint=random.randint(200,-200)
        random_ypoint=random.randint(200,-200)
        self.goto(random_xpoint,random_ypoint)
