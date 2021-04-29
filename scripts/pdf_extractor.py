import fitz
import sys
import pandas as pd

doc = fitz.open(sys.argv[1])
data = []
n_pages = doc.page_count

for i in range(n_pages):
    print(f'{i}/{n_pages}', end="\r", file=sys.stderr)
    page=doc[i]
    for block in page.get_text("blocks"):
        if(block[-1]==0):
            text = block[4].replace('\n', ' ')
            bbox = (block[0], block[1], block[2], block[3])
            n_words = len(text.split())
            data.append([page, bbox, n_words, text])
    
df = pd.DataFrame(data, columns=['page', 'bbox', 'text length', 'text'])
df.to_csv(sys.argv[2], index_label = 'id')
