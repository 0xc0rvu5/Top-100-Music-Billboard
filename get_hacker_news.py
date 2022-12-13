import requests
from bs4 import BeautifulSoup


#initiate global variables
RESPONSE = requests.get('https://news.ycombinator.com/')
SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')
TEXT = SOUP.find_all(name='span', class_='titleline')
SPAN_TEXT = []


#obtain the text from each span with a class named 'titleline' and append it to SPAN_TEXT list
for tag in TEXT:
    text = tag.getText()
    SPAN_TEXT.append(text)


#obtain the upvote numbers of each span with a class name starting with 'score', determine the largest then find its index
UPVOTES = [int(score.getText().split()[0]) for score in SOUP.find_all(name="span", class_="score")]
LARGEST = max(UPVOTES)
FIND_INDEX = UPVOTES.index(LARGEST)


#create a file called 'Hacker_News.txt' in 'w' mode. if it is a new day it will overwrite old content. print the top article first then print all articles separately.
with open('Hacker_News.txt', 'w') as f:
    print('Here are the top articles of the day starting with the article with the most upvotes.\n', file=f)
    print(f'**{SPAN_TEXT[FIND_INDEX]}**', file=f)
    print('\nAll articles located below.\n', file=f)
    for el in SPAN_TEXT:
        print(el, file=f)