#choose file to open
file = open('berita_ngrams.txt', 'r')
tweet_phrases = file.read();
from nltk.collocations import *
from nltk.tokenize import RegexpTokenizer
import nltk


tokens = RegexpTokenizer(r'\w+')
token = tokens.tokenize(tweet_phrases)
tweet = ' '.join(token)
tweet = tweet.lower();
print (tweet)
bifinder = BigramCollocationFinder.from_words(tweet.split(), window_size = 2)
trifinder = TrigramCollocationFinder.from_words(tweet.split(), window_size = 3)
finder1 = BigramCollocationFinder.from_words(tweet.split(), window_size = 2)

finder1.apply_freq_filter(2)
#for Bigram use this syntax --> bigram_measures = nltk.collocations.BigramAssocMeasures()
#for Trigram use this syntax --> trigram_measures = nltk.collocations.TrigramAssocMeasures()
bigram_measures = nltk.collocations.TrigramAssocMeasures()

#choose file to write the calculations results
text_file = open("OutputTrigram.txt", "w")
#for bigram use this syntax --> for k,v in bifinder.ngram_fd.items():
#for trigram use this syntax --> for k,v in trifinder.ngram_fd.items():
for k,v in trifinder.ngram_fd.items():
  tup = (k,v)
  s = " : ".join(map(str, tup))
  print(k,v)
  text_file.write(s+"\n")
text_file.close()