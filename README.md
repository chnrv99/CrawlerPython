# Crawler_Python

## Actual script is final.py  
To run
```
python3 final.py
```

# It is a crawler which can :
1. Crawl through any .onion site and accordingly classify them either as:
 a. Drug Market
 b. Weapons Market
 c. Human Traffiking/ Fraudulent Sites.
 It keeps crawling till a treshold set by the user is met.
 
2. Classify and flag any wesbsite given by user and store it in SQLITE3 DB, and prepare a classified report in form of MS WORD

3. Takes input as Child name, age, blood group etc and searches the darkweb about the child details, and if found it prepares a 
   classified report in MS WORD about the findings
4. Enumerates any .onion website and finds the IP address, Server Version(ISP), and critical vulnerabilities if any

5. Add any potential .onion website manually to DB.

Protections used: 
1. Connected to TOR Control Port(Default 9051) with strong password
2. Changes the IP Address for every 10s

Dependies:
Requests, BS4, pandas, tensorflow, subprocess, spacy, sqlite3, docx, signal and controller from stem

