from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Twitter API credentials
consumer_key = ""
consumer_secret = ""


# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="74381237-NoD1lqLycundzFCcsoxEhoVGZR3K1fw9c8BmpaIug"
access_token_secret= "tGV3lJG3BLAaJ4qInfgkdo9zpArMcrXdmcH1HeHRIuaHB"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['flipkart'])
