from turtle import Turtle
import random

colors = ['green','orange','yellow','pink','purple','gold','gray','brown','white']

class Brick(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(1,2.5)
        self.penup()
        self.goto(x, y)
        self.destroyed = False