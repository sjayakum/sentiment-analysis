from nltk import corpus

__author__ = 'Suraj Jayakumar'

from matplotlib import pyplot
from random import shuffle
from random import sample
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import nltk
import nltk.corpus

import time
start_time = time.time()

def word_features(words):
    return dict([(word.decode('utf8'), True) for word in words])


negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

negativeFeaturePoints = []
positiveFeaturePoints = []
for i in negids:
   negativeFeaturePoints += [(word_features(movie_reviews.words(fileids=[i])), 'bad')]


#negativeFeaturePoints += [(word_features(movie_reviews.words(fileids='neg/suraj.txt')),'shit movie')]
#positiveFeaturePoints += [(word_features(movie_reviews.words(fileids='pos/_rowan.txt')),'great movie')]

for i in posids:
    positiveFeaturePoints += [(word_features(movie_reviews.words(fileids=[i])), 'good')]

negcutoff = len(negativeFeaturePoints) * 3 / 4
poscutoff = len(positiveFeaturePoints) * 3 / 4
negativeFeaturePointsSubSet = negativeFeaturePoints[:negcutoff]
positiveFeaturePointsSubSet =  positiveFeaturePoints[:poscutoff]


trainfeats = negativeFeaturePointsSubSet + positiveFeaturePointsSubSet

testfeats = negativeFeaturePoints[negcutoff:] + positiveFeaturePoints[poscutoff:]
shuffle(testfeats)


# print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))

#classifier = NaiveBayesClassifier.train(positiveFeaturePoints+negativeFeaturePoints)
classifier = NaiveBayesClassifier.train(sample(trainfeats,len(trainfeats)))
# print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
# classifier.show_most_informative_features()
#testTweet1 = "this movie has nothing totally waste of time do something better this weekend if possible"
#testTweet2 = "abysmal performance in chennai express"
#testTweet3 = "what a movie! please watch "
#tweetList = [testTweet1, testTweet2, testTweet3]
#testTweet = "It's likely that buried somewhere under all those unfunny jokes, simplistic sermons, and cringe-inducing melodrama, there may have been a promising idea at the heart of Bangistan.The film's title refers to a fictional country besieged by conflict between the Hindus and the Muslims, who each occupy one half of the land. Religious leaders of both parts are friendly, however, and plan to spread their message of peace at the World Religions Conference in Poland.Meanwhile, extremist groups from either side target the same conference, dispatching a suicide bomber each, who, for reasons that never make complete sense, are disguised as members of the opposite religion. So call-centre employee Hafeez Bin Ali (Ritesh Deshmukh) goes undercover as a Hindu, and Praveen Chaturvedi (Pulkit Samrat), a struggling actor in a ramleela troupe, heads to Krakow pretending to be a Muslim.The script is at best intermittently funny, giving us only a few stray moments of genuine humor. For the most part, the jokes are juvenile. The film's message too is well intentioned but way too simplistic, and you're bludgeoned on the head with it in a shrill climax that feels out of place in a comedy.Of the cast, Ritesh Deshmukh does the best he can to make the thin plot work. The same, unfortunately, can't be said for Pulkit Samrat who has all the subtlety of a sledgehammer. Jacqueline Fernandez, playing a local waitress in a Polish bar, shows up strictly in time for the song situations.Film critic-turned-filmmaker Karan Anshuman shows flashes of wit and potential in his occasionally clever nods to classic films. But saddled with a script that's neither funny nor biting enough, he delivers a film that barely takes off.I'm going with a generous two out of five for Bangistan. Very little bang for your buck here."
#print("--- %s seconds ---" % (time.time() - start_time))

import csv
import time
from random import randint
i = 0
with open('KattiBattiTweets.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        testTweet = row[2]
        words = testTweet.split(" ")
        myTempDicti = {}
        for eachword in words:
            myTempDicti[eachword] = True

        outputClass =  classifier.classify(myTempDicti)
        if outputClass == 'good':
            myfile =  open("twitScores.txt", "a")
            myfile.write(str(i)+","+str(2)+"\n")
            myfile.close()
            #print outputClass
        elif outputClass == 'bad':
            myfile =  open("twitScores.txt", "a")
            myfile.write(str(i)+","+str(1)+"\n")
            myfile.close()
            #print outputClass
        i = i + 1
        time.sleep(2)










