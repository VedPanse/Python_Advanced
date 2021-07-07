from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in article:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

maxima = max(article_upvote)

ind = article_upvote.index(maxima)
print(article_texts[ind])
print(article_links[ind])




