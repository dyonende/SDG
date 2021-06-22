"""
Classify text with ODSG
Make sure the docker container is running:
https://hub.docker.com/r/osdg/osdg-tool

Arg1:   csv with text in 'text' column
Arg2:   csv with SDG labels in column 'OSDG'
"""
import requests
import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
df = df.drop_duplicates(subset=['text'], keep=False)    #remove duplicate text

texts = df['text'].values
results = []

for text in texts:
    data = {'text': text}

    response = requests.post('http://localhost:5000/tag', json=data)

    result = response.json()['result']
    
    if result == []:
        result = ""
    else:   #transform result into list format
        temp = result
        result = []
        for item in temp:
            result.append(item['sdg'])
    results.append(result)
           
df['OSDG'] = results

df.to_csv(sys.argv[2], index=False)
