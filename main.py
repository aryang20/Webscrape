#network request --> parse HTML --> Store data

import requests
from bs4 import BeautifulSoup


def scrape():
  url = 'https://example.com/'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup)
  
  
  title = soup.select_one('h1').text
  text = soup.select_one('p').text
  link = soup.select_one('a').text
  print(title)
  print(text)
  print(link)




if __name__ == '__main__':
  scrape()


