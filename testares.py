# Test area for Mathematical Data Science Assignment 2

import csv
import pandas as pd
#from nltk import *
import nltk
#nltk.download('wordnet')
nltk.download()
from nltk.corpus import wordnet as wn

# Read file
dat = pd.read_csv('processed_data.csv', header = None)

# Seperate words
for i in range(0,len(dat)):
    dat[0][i] = dat[0][i].split()

# Compare the strings

# For all stirngs in dat
    # For all other strings in dat
        # sum = 0
        # For all words in str1
            # For all words in str2
                # sum += 

dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')
print(dog.res_similarity(cat, brown_ic))
