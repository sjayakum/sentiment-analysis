
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def preprocess_tweet(tweet):

    #Replace Hashtags
    tweet = tweet.replace('[#]?','')
    #Replace RTs
    tweet = tweet.replace('[RT]?','')
    #Extract Link

    #Replace Links
    tweet = tweet.replace('[https://]?[t.co/]?','')