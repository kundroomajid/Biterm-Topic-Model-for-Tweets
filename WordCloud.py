import csv
import numpy as np
import matplotlib
matplotlib.use('agg')
from wordcloud import WordCloud
from PIL import Image
import pandas as pd
from os import path,getcwd
import os

p = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# mask used to create masked word clouds
mask = np.array(Image.open(path.join(p, "twitter2.png")))

# here a csv file is read which contains words and their corresponding frequencies in document
reader = csv.reader(open('wordfrequency.csv', 'r'))
next(reader, None) 
d = {}
for k,v in reader:
    d[k] = int(v)
    

# #Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.

wc = WordCloud(mask=mask,background_color="white").generate_from_frequencies(d)
# file is saved to working directory
wc.to_file("wordcloud_masked.png")
