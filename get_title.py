import time
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
headers = {'User-Agent': user_agent}

url='http://imgur.com'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
title=''
for data in soup.find_all('title'):
    print(data.get_text().strip())
    

