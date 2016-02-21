__author__ = 'Suraj Jayakumar'
import sys
import json

scores = {}
tweet_scores = []


def makeafinndic(dictionaryfile):
    global scores
    for line in dictionaryfile:
        x = line.split("\t")
        scores[x[0]] = int(x[1])


def main():
    senti_file = open('E:\Twitter Data Project\/AFINN-111.txt')
    tweet_file = open('E:\Twitter Data Project\/TweetsOnly.txt')

    global scores
    global tweet_scores
    tweet_scores = [0] * 1000

    makeafinndic(senti_file)
    i = 0

    for line in tweet_file:
        words = line.split(" ")  # split tweets into words
        for eachword in words:
            if (eachword in scores):
                tweet_scores[i] += scores[eachword]

        i += 1
    for x in tweet_scores:
        print x


if __name__ == '__main__':
    main()
