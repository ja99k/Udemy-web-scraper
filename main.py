import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = (soup.select('.titleline > a'))
links2 = (soup2.select('.titleline > a'))
subline = (soup.select('.subline'))
soup_age = (soup.select('.age'))

def sort_stories_by_points(hnlist):
    return sorted(hnlist, reverse=True, key=lambda k:k['points'])

def create_custom_hn(links, subline):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href')
        comments = subline.getText().replace('.age', '')
        vote = subline[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                parts = comments.split("|")
                comments = parts[-1].strip()
                comments = comments.replace('\xa0', ' ')
                hn.append({'points':points,'title': title, 'link': href, 'comments':comments})
    return sort_stories_by_points(hn)


pprint.pprint((create_custom_hn(links, subline)))