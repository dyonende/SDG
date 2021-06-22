"""
Use the Aurora queries from the queries scripts for SDG-classification

Arg1:   csv with text in 'text' column
"""

import requests
import sys
import pandas as pd
from queries import *

df = pd.read_csv(sys.argv[1])
df = df.drop_duplicates(subset=['text'], keep=False)

texts = df['text'].values
results = []

for text in texts:
    text = text.lower()
    result = []
    
    if in_sdg1(text):
        result.append("SDG_1")        
    if in_sdg2(text):
        result.append("SDG_2")       
    if in_sdg3(text):
        result.append("SDG_3")   
    if in_sdg4(text):
        result.append("SDG_4") 
    if in_sdg5(text):
        result.append("SDG_5") 
    if in_sdg6(text):
        result.append("SDG_6")      
    if in_sdg7(text):
        result.append("SDG_7") 
    if in_sdg8(text):
        result.append("SDG_8") 
    if in_sdg9(text):
        result.append("SDG_9") 
    if in_sdg10(text):
        result.append("SDG_10") 
    if in_sdg11(text):
        result.append("SDG_11") 
    if in_sdg12(text):
        result.append("SDG_12") 
    if in_sdg13(text):
        result.append("SDG_13") 
    if in_sdg14(text):
        result.append("SDG_14") 
    if in_sdg15(text):
        result.append("SDG_15") 
    if in_sdg16(text):
        result.append("SDG_16") 
    if in_sdg17(text):
        result.append("SDG_17") 
        
    if result == []:
        result = ""

    results.append(result)
           
df['aurora'] = results

df.to_csv(sys.argv[2], index=False)


