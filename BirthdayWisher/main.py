import datetime as dt
import smtplib
import pandas as pd
import random

user = "manya79997@gmail.com"
password = "zjcr fkyj vbbs hixw"

bday = pd.read_csv("birthdays.csv")

templates = ["letter_templates/letter_1.txt",
             "letter_templates/letter_2.txt",
             "letter_templates/letter_3.txt"
             ]

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

for index, row in bday.iterrows():

    random_template = random.choice(templates)

    with open(random_template) as letters:
        letter_content = letters.read()
    letter_content = letter_content.replace(f"[NAME]", row["name"])

    if row["month"] == today_month and row["day"] == today_day:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(
                from_addr=user,
                to_addrs="manya79997@yahoo.com",
                msg=("Subject: Happy Birthday\n"
                     f"{letter_content}")
            )
