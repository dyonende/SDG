"""
filter all text that is short than 20 tokens and remove
duplicates

Arg1:   csv with column 'text_length' and 'text'
Arg2:   output file
"""

import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
df = df[df['text_length']>=20]

df = df.drop_duplicates(subset=['text'])
df.to_csv(sys.argv[2], index=False)
    