import time
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
headers = {'User-Agent': user_agent}

# url='http://imgur.com'
url = 'https://vit.ac.in/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

data=''
for data in soup.find_all('h2'):
    print(data.get_text().strip())
for data in soup.find_all('h3'):
    print(data.get_text().strip())
for data in soup.find_all('h4'):
    print(data.get_text().strip())
for data in soup.find_all('h5'):
    print(data.get_text().strip())
for data in soup.find_all('h6'):
    print(data.get_text().strip())


# images = []
# l=soup.find_all('h1')
# for i in l:
#     print(i.string)
# l=soup.find_all('h2')
# for i in l:
#     print(i)
# l=soup.find_all('h3')
# for i in l:
#     print(i)
# l=soup.find_all('h4')
# for i in l:
#     print(i)
# l=soup.find_all('h5')
# for i in l:
#     print(i)
# print(soup.find_all('h2'))
# print(soup.find_all('h3'))
# print(soup.find_all('h4'))
# print(soup.find_all('h5'))
# print(soup.find_all('h6'))