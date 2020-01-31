import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hacker_news = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            scores = int(vote[0].getText().replace(' points', ''))
            if scores > 99:
                hacker_news.append({'title': title, 'link': href, 'votes': scores})
    return sort_stories_by_votes(hacker_news)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))

# ===============================

# Code Samples

# print(soup.body.contents)
# print(soup.find_all('a'))
# print(soup.find('title'))
# print(soup.find(id='score_20514755'))

# ===============================

# Instructor Code

# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')

# links = soup.select('.storylink')
# subtext = soup.select('.subtext')
# links2 = soup2.select('.storylink')
# subtext2 = soup2.select('.subtext')

# mega_links = links + links2
# mega_subtext = subtext + subtext2


# def sort_stories_by_votes(hnlist):
#   return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


# def create_custom_hn(links, subtext):
#   hn = []
#   for idx, item in enumerate(links):
#     title = item.getText()
#     href = item.get('href', None)
#     vote = subtext[idx].select('.score')
#     if len(vote):
#       points = int(vote[0].getText().replace(' points', ''))
#       if points > 99:
#         hn.append({'title': title, 'link': href, 'votes': points})
#   return sort_stories_by_votes(hn)


# pprint.pprint(create_custom_hn(mega_links, mega_subtext))

