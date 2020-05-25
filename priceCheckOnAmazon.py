import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Surf-Excel-Easy-Detergent-Powder/dp/B00TS8ABHC/ref=lp_21246962031_1_1?srs=21246962031&ie=UTF8&qid=1585766354&sr=8-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[2:])
print(title.strip())
print(converted_price)
