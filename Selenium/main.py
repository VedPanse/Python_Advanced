from selenium import webdriver
chrome_driver_path = "/Users/vedpanse/Desktop/Develope/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://www.amazon.com/Controller-Playstation-Charging-Storage-Included-4/dp/B08T1KHHR9/ref=sr_1_2?dchild=1" \
      "&keywords=PS4&qid=1623506130&sr=8-2"
URL2 = "https://www.amazon.com"
URL3 = "https://www.python.org/"

driver.get(URL3)
#
# search_bar = driver.find_element_by_name("field-keywords")
# print(search_bar.size)
#

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.close()
driver.quit()
