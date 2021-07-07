from selenium import webdriver

chrome_driver_path = "/Users/vedpanse/Desktop/Develope/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://python.org/"
driver.get(URL)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }


print(events)

driver.quit()
