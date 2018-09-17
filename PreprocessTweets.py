#simple script used to preprocess lines from a text file 
#and remove stopwords from a text file
#python v3.6
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
 
 

with open('data/tweets.txt','r') as inFile, open('tweets_processed.txt','w') as outFile:
	for line in inFile.readlines():
		 #Convert to lower case
		line = line.lower()
		#Convert www.* or https?://* to URL
		line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',line)
		#remove @username 
		line = re.sub('@[^\s]+',' ',line)
		#Remove additional white spaces
		line = re.sub('[\s]+', ' ', line)
		#Replace #word with word
		line = re.sub(r'#([^\s]+)', r'\1', line)
		#trim
		line = line.strip('\'"')
		word = word_tokenize(line)
		print(" ".join([word for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split() 
        if len(word) >=3 and word not in stopwords.words('english')]), file=outFile)
