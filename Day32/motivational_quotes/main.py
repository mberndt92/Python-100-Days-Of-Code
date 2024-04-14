import random
import smtplib

# smtp.gmail.com
# PW - ndwr gnyo yjei cqie
#
import datetime as dt
from random import choice


def send_mail(msg):
    print(f"Sending mail with msg: {msg}")
    my_email = "maximilian.berndt92@gmail.com"
    password = "ndwrgnyoyjeicqie"

    subject = "Monday Motivational Quote"
    formatted_msg = f"Subject: {subject}\n\n{msg}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="maximilian_berndt@icloud.com",
            msg=formatted_msg
        )


def get_random_quote():
    with open("./quotes.txt") as file:
        quotes = file.readlines()
        return choice(quotes)


now = dt.datetime.now()
print(now.weekday())
if now.weekday() == 4:
    quote = get_random_quote()
    send_mail(msg=quote)

