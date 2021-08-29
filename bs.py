from bs4 import BeautifulSoup
import requests
import lxml

with open('../tiki.html', encoding="utf8") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# Product link
links = soup.find_all('a', class_='product-item')

# Produce name
names = []
for a in soup.find_all('div', class_='name'):
    names.append(a.span)



# Product price
prices = soup.find_all('div', class_="price-discount__price")

# Output
print('Tiki Products info ')
print()

for name, price, link in zip(names, prices, links):
    print('Product: ', name.text)
    print('Price: ', price.text)
    print('Link:', link['href'])
    print( )

