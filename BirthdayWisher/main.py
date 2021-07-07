from datetime import datetime
import random
import smtplib
import pandas
# Extra Hard Starting Project ######################
MY_EMAIL = "example@example.com"
MY_PASS = "password"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    temp = random.choice(letter_list)
    file_path = f"letter_templates/{temp}"
    f = open(file_path)
    contents = f.read()
    contents = contents.replace('[NAME]', birthday_person["name"])
    f.close()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="pythonved@yahoo.com", msg=f"Subject: Hello\n\n{contents}")
        connection.close()
        print("Mail successfully sent.")

else:
    print("Today is not a birthday.")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




