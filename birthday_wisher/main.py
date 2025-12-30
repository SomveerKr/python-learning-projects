import datetime as dt
import pandas as pd
from smtplib import SMTP
from random import randint
from dotenv import load_dotenv
import os
load_dotenv()
my_email = os.getenv("MY_EMAIL")
password=os.getenv("EMAIL_PASSWORD")
MY_NAME ="Somveer Kumar"

now = dt.datetime.now()
df = pd.read_csv("birthdays.csv")

for index, row in df.iterrows():
    if now.month == row['month'] and now.day == row['day']:
        birthday_name =  row["name"]
        birthday_email = row["email"]
        #pick random letter
        random_letter_path= f"letter_templates/letter_{randint(1, 3)}.txt"
        with open(random_letter_path, "r") as file:
            contents = file.read()            
            letter =contents.replace("[NAME]", birthday_name).replace("Angela", MY_NAME)
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email, to_addrs=birthday_email, msg=f"Subject:Happy Birthday\n\n{letter}")





