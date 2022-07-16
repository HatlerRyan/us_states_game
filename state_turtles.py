from turtle import Turtle



class State(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


    def show_answer(self,state,coor):
        self.goto(coor)
        self.write(state)
        # self.showturtle()


# class StateCount(Turtle):

