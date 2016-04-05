file = open('berita_ngrams.txt', 'r')
tweet_phrases = file.read();
import sys
import codecs
import nltk
from nltk.tokenize import RegexpTokenizer

tokens = RegexpTokenizer(r'\w+')
token = tokens.tokenize(tweet_phrases)
tweet = ' '.join(token)
tweet = tweet.lower();
print (tweet)
fdist = nltk.FreqDist(tweet.split())

text_file = open("OutputUnigram.txt", "w")
for k, v in fdist.most_common():
    tup = (k,v)
    s = " : ".join(map(str, tup))
    print(k,v)
    text_file.write(s+"\n")
text_file.close()
