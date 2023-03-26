from bs4 import BeautifulSoup
import requests
import os

html_page = requests.get('http://vit.ac.in/')

soup = BeautifulSoup(html_page.content,'html.parser')



images = soup.findAll('img')
# print(images)
# for image in images:
    # print(image.get('src'))

# while scraping we find 2 types of images: one with https and one without it

l_with_https = []
l_without_https = []

url_base = 'http://vit.ac.in/'
# while scraping we are checking for that above condition
for image in images:
    if 'http' in image.get('src'):
        l_with_https.append(image.get('src'))
    else:
        print(image.get('src'))
        l_without_https.append(url_base + image.get('src'))

# print('\n\n')
# print(l_without_https)

for i in range(4):
    webs = requests.get(l_without_https[i])
    open('images/' + l_without_https[i].split('/')[-1],'wb').write(webs.content)

    # run the model code
    # 
    # 

# deleting the images
for i in range(4):
    os.remove('images/' + l_without_https[i].split('/')[-1])