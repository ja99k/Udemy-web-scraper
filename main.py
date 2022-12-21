import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = (soup.select('.titleline > a'))
links2 = (soup2.select('.titleline > a'))
subtext = (soup.select('.subtext'))

def sort_stories_by_points(hnlist):
    return sorted(hnlist, reverse=True, key=lambda k:k['points'])

def create_custom_hn(links, subtext):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href')
        comments = subtext[inx].getText().replace('&nbps;comments', '')
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'points':points, 'comments':comments})
            # the comments section is not working properly
    return sort_stories_by_points(hn)


pprint.pprint((create_custom_hn(links, subtext)))