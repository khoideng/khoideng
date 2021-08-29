from bs4 import BeautifulSoup
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "zombiegarudaminecraft@gmail.com"  # Enter your address
receiver_email = "mecureo@gmail.com"  # Enter receiver address
password = 'ilovemymom'
message = """
This product's price is equal with the price you wanted!
Hi there

This message is sent from Python.
This product's price is equal with the price you wanted.
Visit  https://www.amazon.com/Apple-inches-MacBook-display-dual-core/dp/B07XQHL645/ref=sr_1_10?dchild=1&keywords=macbook&qid=1625834382&s=specialty-aps&sr=1 for more

Best regards,
Khoidpn"""

context = ssl.create_default_context()


with open('amazon.html', encoding='utf8') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

wanted = int(input('Please write the price you want for this product: '))
price = soup.find('span', id='priceblock_ourprice').text.split('$')[1]
price = float(price)
if price == wanted:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

print(price)