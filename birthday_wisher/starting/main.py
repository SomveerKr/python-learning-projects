import datetime as dt
from random import choice
from smtplib import SMTP
my_email = "7somveerkumar@gmail.com"
password="gqou vnjp abnq nimz"
to_email ="somveer_kr@yahoo.com"

now = dt.datetime.now()
today  = now.strftime("%A")

if today=="Thursday":
    with open("quotes.txt", "r") as file:
        all_quotes =  file.readlines() #or .read().split("\n")
        quotes_and_authors = []
        for qoute in all_quotes:
            quote_and_author = qoute.split(" - ")
            quote_dict ={
                "quote":quote_and_author[0],
                "author":quote_and_author[1]
            }
            quotes_and_authors.append(quote_dict)

    # print(quotes_and_authors)
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Quote of the Day\n\n{choice(quotes_and_authors)["quote"]}\n   - {choice(quotes_and_authors)["author"]}")

