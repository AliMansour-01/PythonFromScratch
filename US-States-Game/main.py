import turtle
from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("50_states.csv")

image = "blank_states_img.gif"
screen = Screen()
screen.title("U.S States Game")


screen.addshape(image)
turtle.shape(image)

all_states = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:

   user_guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
   if user_guess == "Exit":
      missing_state = [state for state in all_states if state not in guessed_states]
      new_data = pandas.DataFrame(missing_state)
      new_data.to_csv("States to learn")
      break
   if user_guess in all_states:
      guessed_states.append(user_guess)
      t = Turtle()
      t.hideturtle()
      t.penup()
      state_row = data[data.state == user_guess]
      t.goto(state_row.x.item(), state_row.y.item())
      t.write(user_guess)

