from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global link_text
    global links
    link_text = []
    links = []
    query = request.form['query']

    url = 'https://google.com/search?q=' + query
    request_result = requests.get(url)

    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")

    heading_object = soup.find_all('h3')



if __name__ == "__main__":
    app.run(debug=True)
