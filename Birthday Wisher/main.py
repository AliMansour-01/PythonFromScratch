
import datetime as dt
import pandas
import random
import smtplib

email = "alimansour.shaka@gmail.com"
password = "isxfuraytprfzucl"

now = dt.datetime.now()
month = now.month
today = now.day
today_tuple = (month, today)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
print(birthdays_dict)

if (today_tuple) in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy birthday\n\n{contents}")
