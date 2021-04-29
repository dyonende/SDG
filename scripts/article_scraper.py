import sys
import requests
from bs4 import BeautifulSoup
import article_parser
from newspaper import Article
import json
import pandas as pd


with open(sys.argv[1]) as infile:
    links = infile.read()
    links = links.split('\n')
    
data = []

i = 1
for link in links:
    print(f'{i}/{len(links)}', end="\r", file=sys.stderr)
    i+=1
    try:
        article = Article(link)
        article.download()    
        article.parse()
        if article.text.lower().find("cookie") == -1 and article.text.lower().find("javascript") == -1 and article.title.lower().find("subscribe to read")==-1:
            for text in article.text.split('\n'):
                data.append([link, article.title, len(text.split()), text])
        
        '''
        title, content = article_parser.parse(url=link)
        print(title)
        print('----------------')
        print(content)
        input()
        '''
    except KeyboardInterrupt:
        sys.exit()
    except:
        print("error:", link, file=sys.stderr)
        
df = pd.DataFrame(data, columns=['link', 'title', 'text length', 'text'])
df = df.drop_duplicates(subset=['text'])
df.to_csv(sys.argv[2], index_label='id')
