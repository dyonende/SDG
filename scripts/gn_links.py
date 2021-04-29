from bs4 import BeautifulSoup
import requests
import sys
import json

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
    print(f'{counter}/{len(data)}', file=sys.stderr, end='\r')
    counter+=1
    article = article.prettify()
    article = set(article.split())
    for i in article:
        try:
            if i.startswith("href"):
                i = i.split('"')[1][1:]
                link = domain + i
                r = requests.get(link, allow_redirects=True, cookies=cookies)
                link = r.url
                if link.startswith('https://news.google.com/publications/')==False:
                    links.add(link)   
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("error", link, file=sys.stderr)
for link in links:
    print(link)

'''
#API_key = '0a0336b224be453991c97d37055e064f'

url = ('https://newsapi.org/v2/everything?'
       f'q={sys.argv[1]}&'
       'apiKey=0a0336b224be453991c97d37055e064f')
       
response = requests.get(url)
obj = json.loads(response.content.decode('UTF-8'))

print(json.dumps(obj, indent=4))
'''