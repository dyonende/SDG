"""
Draw a cooccurrence matrix of SDGs

Args: csv with SDG labels in column 'combined'
"""
import sys
import pandas as pd
import ast
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py

cooccurrence = dict()
for path in sys.argv[1:]:
    filename = os.path.basename(path)
    df = pd.read_csv(path)
    df = df.dropna(subset=["combined"])
    labels = df["combined"].values


    for i in range(len(labels)):
        current_labels = ast.literal_eval(labels[i])
        
        for label in current_labels:
            label = int(label.split('_')[1])
            for label_2 in current_labels:
                label_2 = int(label_2.split('_')[1])
                if label in cooccurrence:
                    if label_2 in cooccurrence[label]:
                        cooccurrence[label][label_2]+=1
                    else:
                        cooccurrence[label][label_2]=1
                else:
                    cooccurrence[label]=dict()
                    cooccurrence[label][label_2]=1
                if label == label_2:
                    cooccurrence[label][label_2]=0
                 
df = pd.DataFrame.from_dict(cooccurrence)  
df.sort_index(inplace=True)  
df = df.fillna(0)
df = df[sorted(df.columns)]    

######
#PLOT#
######         

matrix = np.array(df)

fig, ax = plt.subplots()
im = ax.imshow(matrix)


# Loop over data dimensions and create text annotations.
for i in range(17):
    for j in range(17):
        text = ax.text(j, i, int(matrix[i, j]),
                       ha="center", va="center", color="w")

fig.tight_layout()
plt.savefig('test.png')
print(df)

    
    

        
