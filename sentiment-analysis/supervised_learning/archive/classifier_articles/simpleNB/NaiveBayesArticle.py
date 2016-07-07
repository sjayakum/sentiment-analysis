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

"""
I/P sentence = " Hey this really good. I'd love to watch it again"

STEP 1 -> Tokenize
STEP 2 -> Create a dictionary with each word as 'KEY' and True as 'VALUE'
STEP 3 -> Create tuple as (Dictionary,CLASS)
STEP 4 -> Append it to a list.

Repeat and keep appending the new tuple back to the list.
[  (   DICTIONARY-1    ,'negative' ) ,  (  DICTIONARY-2 ,'negative' )    ]

DICTIONARY-1
{
    "Hey" : True
    "this" : True
    "really" : True
}
"""

def load_data():
   global posfeats,negfeats
   negids = movie_reviews.fileids('neg')
   posids = movie_reviews.fileids('pos')
   negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
   posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
   return


def create_training():
    global  trainfeats,negfeats,posfeats
    shuffle(negfeats)
    shuffle(posfeats)
    trainfeats.extend(posfeats)
    trainfeats.extend(negfeats)
    shuffle(trainfeats)

def build_classifier():
    global classifier,trainfeats
    classifier = NaiveBayesClassifier.train(trainfeats)
    classifier.show_most_informative_features()

load_data()
create_training()
build_classifier()
pickle.dump(classifier,open('NaiveBayesGood.p','wb'))
