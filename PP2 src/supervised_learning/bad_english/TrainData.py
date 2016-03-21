from PreProcessing import preprocess
from Vectorize import word2vec
from __future__ import print_function
from random import shuffle
from nltk.classify import NaiveBayesClassifier
import pickle
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

    try:
        f = open('training.txt','r')
    except:
        print ("No file named in training.txt in current directory")

    pos = []
    neg = []
    corpus = []
    for eachline in f:
        senti,text = eachline.split('\t')
        corpus.append(text)
        if(int(senti)==0):
            temp = preprocess(text)
            neg.append((word_feats(temp),'neg'))
        elif(int(senti)==1):
            temp = preprocess(text)
            pos.append((word_feats(temp),'pos'))


    try:
        f2  = open('training3.csv','r')
    except:
        print("Cant open training3.csv")

    i = 0
    for eachline in f2:
        i+=1
        temp = eachline.split(',')
        text = str(temp[5]).strip()
        senti = int(temp[0].strip('""'))
        if(int(senti)==0):
            pptweet = preprocess(text)
            neg.append((word_feats(pptweet,'neg')))
        elif(int(senti)==4):
            pptweet = preprocess(text)
            pos.append((word_feats(temp),'pos'))
        if(i>100000):
            break


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
pickle.dump(classifier,open('NaiveBayesBad.p','wb'))







# try:
#     f = open('training.txt','r')
# except:
#     print ("No file named in training.txt in current directory")
#
# pos = []
# neg = []
# corpus = []
# for eachline in f:
#     senti,text = eachline.split('\t')
#     corpus.append(text)
#     if(int(senti)==0):
#         temp = preprocess(text)
#         for eachword in temp:
#             neg.append(eachword)
#     elif(int(senti)==1):
#         pos.append(text)
#
# corpus_pre = []
# for eachsentence in corpus:
#     corpus_pre.append(preprocess(eachsentence))
#
# w2vmodel = word2vec(corpus_pre)
#
# print (w2vmodel['stupid'])

