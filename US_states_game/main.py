import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game ")
screen.setup(width = 700, height = 500)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state = data.state
states = state.to_list()

guesses = []

while len(guesses) < 50:
    guess = screen.textinput(f"{len(guesses)}/ 50 States correct",
                             "What's another state's name?").title()

    if guess in states:
        guesses.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(guess)

screen.exitonclick()
