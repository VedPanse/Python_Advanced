import random
from datetime import datetime as dt
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


@app.route("/guess/<name_from_api>")
def guess(name_from_api):
    g_response = requests.get(f"https://api.genderize.io?name={name_from_api}")
    g_data = g_response.json()

    a_response = requests.get(f"https://api.agify.io?name={name_from_api}")
    a_data = a_response.json()
    gender = g_data["gender"]
    age = str(a_data["age"])
    name = a_data["name"].capitalize()

    return render_template("AgeifyGenderify.html", gender=gender, age=age, name=name)


@app.route("/homepage")
def show_home():
    return "Welcome to my homepage"


if __name__ == "__main__":
    app.run(debug=True)
