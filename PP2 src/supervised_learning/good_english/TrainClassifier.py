import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

import pickle
from random import shuffle

#GLOBAL DECLARATION
trainfeats =[]
posfeats = []
negfeats = []
classifier = 0
#every word before feeding in to NaiveBayes Classifier should be of this form
def word_feats(words):
    """
    :param words: takes any english sentence
    :return: a dictionary by splitting each word in the sentence where 'word' is the key and 'True' is the value
    """
    return dict([(word, True) for word in words])

##Uses nltk.corpus.movie_reviews => Already Classified as Pos and Neg
#def getMovieReviewCorpus():
#    global posfeats,negfeats
#    negids = movie_reviews.fileids('neg')
#    posids = movie_reviews.fileids('pos')
#    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
#    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
#    return


def univMichTrainingCorpus():
    global posfeats,negfeats

    fobj = open(r'home/suraj/Projects/sentiment-analysis/PP2 src/training.txt')
    for eachline in fobj:
        abc = eachline.split('\t')
        sentimentValue = int(abc[0])
        appendVariable = str(abc[1]).strip()
        bag_of_words = preprocess(appendVariable)
        if(sentimentValue==0):
                negfeats.append((bag_of_words,'neg'))
        elif(sentimentValue==1):
                posfeats.append((bag_of_words,'pos'))

#def hugeTrainingCorpus():
#    global posfeats,negfeats
#    fobj= open(r'E:\Capstone Project\capstoneproject\src\chatDataClassifier\trainingData\trainingSet\training1600000.csv')
#    for eachSentence in fobj:
#        x = eachSentence.split(',')
#        appendVariable = str(x[5]).strip()
#        sentimentValue = int(x[0].strip('""'))
#        print sentimentValue
#        if(sentimentValue==0):
#            negfeats.append((word_feats(appendVariable),'neg'))
#        elif(sentimentValue==4):
#            posfeats.append((word_feats(appendVariable),'pos'))


def createTrainingset():
    global  trainfeats,negfeats,posfeats
    shuffle(negfeats)
    shuffle(posfeats)
    trainfeats.extend(posfeats)
    trainfeats.extend(negfeats)
    shuffle(trainfeats)

def buildClassifier():
    global classifier,trainfeats
    classifier = NaiveBayesClassifier.train(trainfeats)
    #print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
    #classifier.show_most_informative_features()







#getMovieReviewCorpus()

univMichTrainingCorpus()


#hugeTrainingCorpus()

createTrainingset()
buildClassifier()
pickle.dump(classifier,open('UMich.pickle','wb'))