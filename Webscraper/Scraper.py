import requests
from bs4 import BeautifulSoup
r = requests.get('https://sociallydistant.site')
print(r.url)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
