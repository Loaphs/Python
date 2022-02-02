import requests
from bs4 import BeautifulSoup as bs


url='https://oxylabs.io/blog'
response = requests.get(url)

soup = bs(response.text, 'html.parser')
print(soup.h1)