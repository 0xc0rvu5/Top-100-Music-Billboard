import requests, random
from bs4 import BeautifulSoup


#initialize global variables
RESPONSE = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')
TEXT = SOUP.find_all(name='h3', class_='title')
H3_TEXT = []


#obtain the text from each span with a class named 'title' and append it to H3_TEXT list
for tag in TEXT:
    text = tag.getText()
    H3_TEXT.append(text)


#create a file called 'Top_Movies.txt' in 'w' mode. if it is a new day it will overwrite old content. print a random movie first then print all movies separately.
with open('Top_Movies.txt', 'w') as f:
    print('Here are the top 100 movies to watch starting with a random choice to watch first.\n', file=f)
    print(f'**{random.choice(H3_TEXT)}**', file=f)
    print('\nAll movies located below.\n', file=f)
    for el in reversed(H3_TEXT):
        print(el, file=f)
