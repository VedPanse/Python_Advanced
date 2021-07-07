import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def question():
    return "<h1>Guess a number between 0 and 9</h1><img " \
           "src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'> "


@app.route("/<number>")
def get_user_number(number):
    num = random.randint(0, 10)
    number = int(number)
    if num == number:
        return "<h1 style='color: dodgerblue, font-family: Roboto'>You found me</h1><img " \
               "src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'> "
    elif num > number:
        return "<h1 style='color: tomato, font-family: Roboto'>Too Low</h1><img " \
               "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'> "
    elif num < number:
        return "<h1 style='color: purple, font-family: Roboto'>Too High</h1><img " \
               "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'> "




if __name__ == "__main__":
    app.run(debug=True)
