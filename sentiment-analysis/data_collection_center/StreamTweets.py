#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


# MAX OF 3240
# AT A TIME 200

finalArray = []
def get_all_tweets(screen_name):
    global finalArray
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    finalArray.extend(new_tweets)
    # save most recent tweets
    alltweets.extend(new_tweets)
    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(alltweets) < 2500:
        print "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        # save most recent tweets
        alltweets.extend(new_tweets)
        finalArray.extend(new_tweets)
        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))
        # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.created_at, tweet.text.encode("utf-8"), tweet.favorite_count, tweet._json[u'geo'],
                  tweet._json[u'retweet_count']] for tweet in alltweets]

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["time", "text", "favorites", "geo", "retweets"])
        writer.writerows(outtweets)


    pass


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("Swamy39")
