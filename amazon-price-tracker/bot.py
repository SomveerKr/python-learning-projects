
from dotenv import load_dotenv
# 1. Load the variables from .env into the environment
load_dotenv()
import requests
from bs4 import BeautifulSoup
from send_mail import SendMail

send_email = SendMail()
amazon_clone_url = "https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDQ429?th=1"
my_headers ={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9",
"Priority": "u=0, i",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
}
response = requests.get(amazon_clone_url, headers=my_headers)
data  = response.text

soup = BeautifulSoup(data, "html.parser")

price_tag = soup.select_one("span.reinventPricePriceToPayMargin span.a-price-whole")
price =int(price_tag.text.replace(",", ""))
product_title = (soup.find("span", id="productTitle")).text
print(soup.find("span", id="productTitle"))
print(product_title)
print(price)
if price <80000:
    send_email.send_mail(receiver_email= "work.somveerk@gmail.com", current_price= price, product_title= product_title)






