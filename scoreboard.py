from turtle import Turtle
FONT = ('Arial', 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self,):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.goto(150, 275)
        self.states_guessed = 0
        self.write(f"{self.states_guessed}/50", font=FONT)

    def correct(self):
        self.states_guessed += 1
        self.write(f"{self.states_guessed}/50", font=FONT)
