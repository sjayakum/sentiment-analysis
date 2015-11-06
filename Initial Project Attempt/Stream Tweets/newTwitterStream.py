__author__ = 'Suraj Jayakumar'
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "74381237-NoD1lqLycundzFCcsoxEhoVGZR3K1fw9c8BmpaIug"
access_token_secret = "tGV3lJG3BLAaJ4qInfgkdo9zpArMcrXdmcH1HeHRIuaHB"
consumer_key = "b6JCMorNFh6FcUSe9sUvkrdfU"
consumer_secret = "LUqE9wdU8KummZh6DRdkS2HEaVL7uBxS2eFPwMeSFbbhfz9gxi"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['Bajrangi Bhaijaan', '', ''])
    stream.filter(languages="english")