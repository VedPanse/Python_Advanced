from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)

print(soup.prettify)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
print("\n---------------")

for tag in all_anchor_tags:
    # Get text
    print(tag.getText())
    # Get link
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text)

# Find a specific tag

# First matching item
company_url = soup.select_one(selector="p em a")
# Or selector = #name (for id)
print(company_url)


















