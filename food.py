from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape()
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)