import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return "Get started by putting your name in front of the guess"


@app.route("/guess/<name_from_api>")
def home(name_from_api):
    g_response = requests.get(f"https://api.genderize.io?name={name_from_api}")
    g_data = g_response.json()

    a_response = requests.get(f"https://api.agify.io?name={name_from_api}")
    a_data = a_response.json()
    gender = g_data["gender"]
    age = str(a_data["age"])
    name = a_data["name"].capitalize()

    return render_template("AgeifyGenderify.html", gender=gender, age=age, name=name)


if __name__ == "__main__":
    app.run(debug=True)
