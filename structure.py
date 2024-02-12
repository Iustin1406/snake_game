from turtle import Turtle


class Structure(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.width(20)
        self.color(100, 65, 23)
        self.create_margins()

    def create_margins(self):
        self.penup()
        self.goto(0, -280)
        self.forward(280)
        self.left(90)
        self.pendown()

        self.forward(540)
        self.left(90)
        self.forward(570)
        self.left(90)
        self.forward(540)
        self.left(90)
        self.forward(570)
        self.left(90)
