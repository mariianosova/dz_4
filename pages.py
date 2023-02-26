import requests
from bs4 import BeautifulSoup

i = 1

while True:
    url = f'https://quotes.toscrape.com/page/{i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    button_next = soup.find('li', class_="next")

    if button_next != None:
        i += 1
    else:
        break

print(f'На сайте {i} страниц')
