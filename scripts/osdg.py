import requests
import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
df = df.drop_duplicates(subset=['text'], keep=False)

texts = df['text'].values
results = []

for text in texts:
    data = {'text': text}

    response = requests.post('http://localhost:5000/tag', json=data)

    result = response.json()['result']
    if result == []:
        result = ""
    else:
        temp = result
        result = []
        for item in temp:
            result.append(item['sdg'])
    results.append(result)
           
df['OSDG'] = results
#df = df[df['OSDG']!=""]

df.to_csv(sys.argv[2], index=False)
