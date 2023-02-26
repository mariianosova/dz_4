import requests
from bs4 import BeautifulSoup


def quotes():

    i = 1
    quotes = []

    while True:
        url = f'https://quotes.toscrape.com/page/{i}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
                
        items = soup.find_all('div', class_='quote')

        for item in items:
            item_text = item.find('span', class_="text").text
            item_author = item.find('small', class_="author").text
            quotes.append(f'{item_text} - (c) {item_author}')

        button_next = soup.find('li', class_="next")

        if button_next != None:
            i += 1
        else:
            break

    return quotes, i

quotes, i = quotes()

for j, x in enumerate(quotes):
    print(f'{j+1}. {x}')

print(f'На сайте {i} страниц и {j+1} цитат')
