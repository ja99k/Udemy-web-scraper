import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = (soup.select('.titleline > a'))
votes = (soup.select('.score'))

def sort_stories_by_points(hnlist):
    return sorted(hnlist, reverse=True, key=lambda k:k['points'])

def create_custom_hn(links, votes):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href')
        points = int(votes[inx].getText().replace(' points', ''))
        if points < 100:
            continue
        # print(points)
        hn.append({'title': title, 'link': href, 'points':points})
    return sort_stories_by_points(hn)


pprint.pprint((create_custom_hn(links, votes)))