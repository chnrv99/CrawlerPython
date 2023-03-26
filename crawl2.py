import time
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import os
import csv
import pandas as pd

filename = 'ClassifiedData.csv'
First_Row = ['Drug names']
Row = []
Rows = []

def get_heading(link):
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("The heading of "+link+" is: ")
    l=[]
    data=''
    # for data in soup.find_all('h2'):
    #     l.append(data.get_text().strip())
    #     print(data.get_text().strip())
    # for data in soup.find_all('h3'):
    #     l.append(data.get_text().strip())
    #     print(data.get_text().strip())
    for data in soup.find_all('h4'):
        l.append(data.get_text().strip())
        print(data.get_text().strip())
    # for data in soup.find_all('h5'):
    #     l.append(data.get_text().strip())
    #     print(data.get_text().strip())
    # for data in soup.find_all('h6'):
    #     l.append(data.get_text().strip())
    #     print(data.get_text().strip())


    print("\n\n")
    return l

def get_images(link):
    html_page = requests.get(link)

    soup = BeautifulSoup(html_page.content,'html.parser')



    images = soup.findAll('img')
    # print(images)
    # for image in images:
        # print(image.get('src'))

# while scraping we find 2 types of images: one with https and one without it

    l_with_https = []
    l_without_https = []

    url_base = link
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


def get_title(link):
    l1=[]
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    title=''
    print("The title of "+link+" is: ")
    for data in soup.find_all('title'):
        l1.append(data.get_text().strip())
        print(data.get_text().strip())
    # data = soup.find_all('title').get_text.strip()
    print('\n\n')
    return l1



# Set the number of links to crawl
num_links_to_crawl = 400

# Set the user agent to use for the request
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

# Set the headers for the request
headers = {'User-Agent': user_agent}

count=0

# Initialize the controller for the Tor network
with Controller.from_port(port=9051) as controller:
    # Set the controller password
    controller.authenticate(password='CristianoRonaldoCR7')

    # Set the starting URL
    url = 'https://thehiddenwiki.com/'

    # Initialize the visited set and the link queue
    visited = set()
    queue = [url]

    # Get the list of keywords to search for
    # keywords = input('Enter a list of keywords to search for, separated by commas: ').split(',')

    # Crawl the links
    while queue:
        # Get the next link in the queue
        link = queue.pop(0)


        # Skip the link if it has already been visited
        if link in visited:
            continue

        # Set the new IP address
        controller.signal(Signal.NEWNYM)
        try:
        # Send the request to the URL
            response = requests.get(link, headers=headers)
            # Parse the response
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all links on the page
            links = soup.find_all('a')

            # Add any links that contain the keywords to the queue
            for a in links:
                # print(a.get('href'))
                href = a.get('href')
                # if any(keyword in href for keyword in keywords):
                if(href==None):
                    continue
                elif('http' in href):
                    queue.append(href)
            # print(queue)
            # getting the title, heading and images
            # get_heading(url)
            # s = get_title(link)
            # get_images(url)
            s1 = get_heading(link)

            # adding it to csv file
            # if s!=[]:
                # Row.append(s[0])
            Row.append(s1)
            # Row.append(link)
            if Row not in Rows:
                Rows.append(Row)
            Row = []


            

            # Add the link to the visited set
            visited.add(link)

            # Print the title and URL of the page
            # print(soup.title.string, link)
            count+=1
            # print('No of links visited: ',count)
            # if count==290:
            #     break

            # Check if the number of visited links has reached the limit
            if len(visited) >= num_links_to_crawl:
                break
        except:
            print("Exception occured for link:",link)
            continue

data = pd.DataFrame(Rows,columns=First_Row)
data.to_csv('links.csv',index=False)

# Print the visited links
print('Visited links:')
for link in visited:
    print(link)