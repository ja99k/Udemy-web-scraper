import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = (soup.select('.titleline'))
score = (soup.select('.score'))

# print(links[0])
print(score[0])