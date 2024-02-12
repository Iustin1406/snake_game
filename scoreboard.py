from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
with open("data.txt", mode="r") as file:
    high_score_from_file = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.high_score = int(high_score_from_file)
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-10, 270)
        self.write(f"Current score : {self.value}   High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.value += 1
        self.clear()
        self.write(f"Current score : {self.value}   High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.value > self.high_score:
            self.high_score = self.value
            with open("data.txt", mode="w") as output:
                output.write(str(self.high_score))
        self.value = 0
        self.clear()
        self.write(f"Current score : {self.value}   High score : {self.high_score}", align=ALIGNMENT, font=FONT)
