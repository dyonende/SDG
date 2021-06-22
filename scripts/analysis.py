import glob
import sys
import pandas as pd
import ast
import os
import csv

data = dict()
for path in sys.argv[1:]:
    filename = os.path.basename(path)
    df = pd.read_csv(path)
    df = df.dropna(subset=["combined"])
    sentiments = df["sentiment"].values
    labels = df["combined"].values

    length = len(sentiments)

    label_sentiments = dict()

    for i in range(length):
        current_labels = ast.literal_eval(labels[i])
        sentiment = sentiments[i]
        for label in current_labels:
            label = int(label.split('_')[1])
            if label in label_sentiments:
                updated_sentiment = label_sentiments[label]
                updated_sentiment.append(sentiment)
                label_sentiments[label]=updated_sentiment
            else:
                label_sentiments[label]=[sentiment]

    df_2 = pd.DataFrame.from_dict(label_sentiments, orient="index")
    df_2.sort_index(inplace=True)
    df_2 = df_2.swapaxes("index", "columns")
    
    new_name = path.replace(".csv", "_matrix.csv")
    df_2.to_csv(new_name, index=False)
    
    

        
