import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as quotes:
    quote = quotes.readlines()

random_quote = random.choice(quote)

email = "manya79997@gmail.com"
password = "zjcr fkyj vbbs hixw"

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #blocks any intervention
        connection.login(user = email , password = password)
        connection.sendmail(
            from_addr = email ,
            to_addrs = "manya79997@yahoo.com",
                msg = f"Subject: Quote \n\n "
                      f"{random_quote}."
        )




