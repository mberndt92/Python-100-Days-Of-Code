##################### Extra Hard Starting Project ######################

import smtplib
import datetime as dt
import pandas as pd
from random import randint
import os


def get_todays_birthdays():
    path = os.getcwd()
    birthdays = pd.read_csv(f"{path}/birthdays.csv").to_dict(orient="records")
    today = dt.datetime.today()
    today_birthdays = []
    for person in birthdays:
        if today.month == person["month"] and today.day == person["day"]:
            today_birthdays.append(person)
    return today_birthdays


def generate_birthday_msg(recipient):
    with open(f"./letter_templates/letter_{randint(1,3)}.txt") as file:
        template_letter = file.read()
        final_msg = template_letter.replace("[NAME]", recipient)

    return final_msg


def send_mail(subject, msg, to):
    my_email = "maximilian.berndt92@gmail.com"
    password = "ndwrgnyoyjeicqie"

    formatted_msg = f"Subject: {subject}\n\n{msg}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="maximilian_berndt@icloud.com",
            msg=formatted_msg
        )


birthdays = get_todays_birthdays()
for birthday in birthdays:
    msg = generate_birthday_msg(recipient=birthday["name"])
    subject = "Happy Birthday"
    recipient = birthday["name"]
    send_mail(subject=f"{subject} {recipient}!", msg=msg, to=birthday["email"])


