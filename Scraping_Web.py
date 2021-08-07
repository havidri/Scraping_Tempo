from bs4 import BeautifulSoup
import requests


url = requests.get('https://www.tempo.co/populer')
bs = BeautifulSoup(url.text, 'html.parser')

berita_populer = bs.find('section', attrs={'class': 'list list-type-1'})
contents = berita_populer.find_all('div', attrs={'class': 'card card-type-1'})


for populer in contents:
    print(populer.find('h2', attrs={'class': 'title'}).text )