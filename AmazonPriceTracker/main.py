from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

USER_NAME = "emailid@mail.com"
PASS_WORD = "your_password"

TARGET_PRICE = 100
URL = "https://www.amazon.com/Controller-Playstation-Charging-Storage-Included-4/dp/B08T1KHHR9/ref=sr_1_2?dchild=1" \
      "&keywords=PS4&qid=1623506130&sr=8-2"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.101 Safari/537.36",
}
response = requests.get(url=URL, headers=headers)
my_web_page = response.text

soup = BeautifulSoup(my_web_page, "lxml")

price = float(soup.find(name="span", id="priceblock_ourprice", class_="a-size-medium a-color-price "
                                                                      "priceBlockBuyingPriceString").text.split("$")[1])
if price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_NAME, password=PASS_WORD)
        connection.sendmail(from_addr=USER_NAME, to_addrs="pythonved@yahoo.com", msg="Subject: PRICE\n\nThe cost of "
                                                                                     "PS5 has dropped below $100.")
        print("Mail successfully sent.")
else:
    print("Not really")
