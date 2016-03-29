__author__ = 'Suraj Jayakumar'
import sys
import json


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def main():
    tweet_file = open('E:\Twitter Data Project\/MissionImpossible.txt')
    output_file = open('E:\Twitter Data Project\/MissionImpossibleTextOnly.txt',"w")
    tweets = {}

    i = 0

    for line in tweet_file:
        line
        print line
        tweets[i] = json.loads(line)
        # Calculatethe score
        if ("text" in tweets[i]):
            mytext = tweets[i]["text"]
            if(is_ascii(mytext)):
                output_file.write(mytext)

    #print mylist[0]
    #print mylist[2]



if __name__ == '__main__':
    main()