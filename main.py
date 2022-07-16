import turtle
import pandas
from state_turtles import State
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(750, 700)
game_on = True
scoreboard = Scoreboard()
states_guessed = []
states = pandas.read_csv("50_states.csv")
state_list = states["state"].to_list()
while game_on:
    answer_state = screen.textinput(title="Guess the State.",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    print(answer_state)

    if answer_state not in state_list:
        pass
    for state in state_list:
        if answer_state == state:
            scoreboard.clear()
            scoreboard.correct()
            answer_coor = states.loc[states["state"] == answer_state]
            xcoor = int(answer_coor.x)
            ycoor = int(answer_coor.y)
            coor = (xcoor, ycoor)
            state = State()
            state.show_answer(answer_state, coor)
            states_guessed.append(answer_state)
            print(states_guessed)
            state_list.remove(answer_state)
            print(state_list)
            if len(states_guessed) == 50:
                game_on = False
new_data = pandas.DataFrame(state_list)
unknown_state = new_data.index
new_data.to_csv("states_to_learn")
