"""
Extract all article links from a Google News HTML file

Arg1: Google News HTML
Output: Links printed to terminal
"""
from bs4 import BeautifulSoup
import requests
import sys
import json

#Cookies to circumvent cookie wall
cookies = {
    'OTZ': '5934823_48_52_123900_48_436380',
    'GN_PREF': 'W251bGwsIkNBSVNEQWkwOHRxREJoQ1FuckNaQWciXQo_',
    'NID': '213=MvfvtabcIWuPhiFTbC9277RXnV0NhciXQw_Hd3WbuitmY2PZDID5EmdFC_wbcHQsDGbMGZZ7Czgdnv9i8R2fCdYSxgEmCAcySLtFzSWtOZYQ5Vw253Mx3UvOcBzlL4liRtMgnACF4rlVtT_9GSfW9ckPkUzi4Lw8_jEauPV1Qyo',
    'CONSENT': 'YES+cb.20210406-12-p0.en-US+FX+313'
}

domain = "https://news.google.com"
links = set()

with open(sys.argv[1]) as infile:
    soup = BeautifulSoup(infile.read(), 'html.parser')
    
soup = soup.find('main')
data = set(soup.find_all('a'))
counter = 1
for article in data:
    #progress indicator to stderr
    print(f'{counter}/{len(data)}', file=sys.stderr, end='\r')
    counter+=1
    
    article = article.prettify()
    article = set(article.split())
    for i in article:
        try:
            if i.startswith("href"):
                i = i.split('"')[1][1:]
                link = domain + i
                #follow redirections to get original url
                r = requests.get(link, allow_redirects=True, cookies=cookies, timeout=100)
                link = r.url
                #ignore links that are from Google publications
                if link.startswith('https://news.google.com/publications/')==False:
                    links.add(link)   
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("error", link, file=sys.stderr)
for link in links:
    print(link)