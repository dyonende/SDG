import sys
import pandas as pd
import ast

df = pd.read_csv(sys.argv[1])

osdg = list(df['OSDG'].fillna(""))
aurora = list(df['aurora'].fillna(""))
combined = []

for i in range(len(osdg)):
    sdgs = set()
    sdg_osdg = osdg[i]
    sdg_aurora = aurora[i]
    if sdg_osdg!="":
        sdg_osdg = set(ast.literal_eval(sdg_osdg))
    else:
        sdg_osdg = set()
        
    if sdg_aurora!="":
        sdg_aurora = set(ast.literal_eval(sdg_aurora))
    else:
        sdg_aurora = set()
        

    sdgs = list(sdg_osdg.union(sdg_aurora))
    if sdgs == []:
        sdgs = ""
    combined.append(sdgs)
    
           
df['combined'] = combined

df.to_csv(sys.argv[2], index=False)