import requests
from bs4 import BeautifulSoup

from threading import Timer
import smtplib
from email.message import EmailMessage


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'
}




def check_price(url,mail,prize):
    URL=url
    set_price = prize
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    price = soup.find(class_="a-offscreen").get_text()
    # print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    if float(product_price) <= int(set_price):
        alert_system(product_title, URL, mail)
        print('sent')
        return
    else:
        print('not sent')
    Timer(60, check_price).start()



def alert_system(product, link, mail):
    email_id = 'test@gmail.com'
    email_pass = 'test1234'

    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = mail # receiver address
    msg.set_content(f'Hey, price of {product} dropped!\n{link}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)



