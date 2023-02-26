from bs4 import BeautifulSoup
import requests


def get_prices():
    url = 'https://scrapingclub.com/exercise/list_basic/'
    params = {'page': 1}
    products = []
    
    while True:
        response = requests.get(url, params=params) # https://scrapingclub.com/exercise/list_basic/?page=1
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        
        
        
        
        for i, item in enumerate(items):
            item_name = item.find('h4', class_='card-title').text.strip('\n')
            item_price = item.find('h5').text
            products.append(f'{item_price} за {item_name}')
        
        last_button = soup.find_all('a', class_='page-link')[-1].text
        
        if last_button == 'Next':
            params['page'] += 1
        else:
            break
            
    return products       


for i, elem in enumerate(get_prices()):
    print(f'{i+1}. {elem}')