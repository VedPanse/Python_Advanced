from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/vedpanse/Desktop/Develope/chromedriver 3"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()
# article_count.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
