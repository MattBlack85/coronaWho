from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup

URL = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'


def scrape():
    response = requests.get(URL)

    if response.status_code != 200:
        raise Exception('Unexpected response')

    soup = BeautifulSoup(response.content, 'html.parser')

    data = soup.find(id='registerData').contents[0]
    now = dt.now().isoformat()

    with open(f'{now}_corona.json', 'w+') as f:
        f.write(data)


if __name__ == '__main__':
    scrape()
