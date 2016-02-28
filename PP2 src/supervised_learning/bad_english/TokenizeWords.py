import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

f = open(r'E:\GitHub\training_datasets\tweets1.6Mil\training1600000.csv')

i = 0




for eachline in f:
    i += 1
    x = eachline.split(',')
    tweet = str(x[5]).strip()

    #PRE PROCESSING
    tweet = tweet.replace('[https://]?[t.co/]?','')
    tweet = tweet.replace('[#]?','')
    tweet = tweet.replace('[RT]?','')

    tweet_tokenized = word_tokenize(tweet)
    stops = set(stopwords.words("english"))
    words = [w for w in tweet_tokenized if not w in stops]
    print words
    if(i == 10):
        sys.exit(0)