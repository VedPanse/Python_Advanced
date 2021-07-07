from selenium import webdriver
chrome_driver_path = "/Users/vedpanse/Desktop/Develope/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://secure-retreat-92358.herokuapp.com/"

driver.get(URL)
fName = driver.find_element_by_name("fName")
lName = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
button = driver.find_element_by_class_name("btn-lg")

fName.send_keys("Ved")
lName.send_keys("Panse")
email.send_keys("pythonved@gmail.com")
button.click()

driver.quit()
