import time
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import os
import csv
import pandas as pd

filename = 'DrugNames.csv'
First_Row = ['Drug names']
Row = []
Rows = []


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
    url = 'http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/'

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
        # Send the request to the URL
        response = requests.get(link, headers=headers)
        # Parse the response
        soup = BeautifulSoup(response.text, 'html.parser')

            # Find all title on the page
        title = soup.find_all('title')
        print(title)
        dfs = pd.read_html(url)
        print(dfs)

        
      
    
data = pd.DataFrame(Rows,columns=First_Row)
data.to_csv('DrugNames.csv',index=False)

# Print the visited links
print('Visited links:')
for link in visited:
    print(link)