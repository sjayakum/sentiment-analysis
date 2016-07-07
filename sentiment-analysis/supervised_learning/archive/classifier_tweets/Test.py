
from __future__ import print_function

from PreProcessing import preprocess
from Vectorize import word2vec

from random import shuffle
from nltk.classify import NaiveBayesClassifier
import pickle

def word_feats(words):
    """
    :param words: takes any english sentence
    :return: a dictionary by splitting each word in the sentence where 'word' is the key and 'True' is the value
    """
    return dict([(word, True) for word in words])

neg = []
pos = []
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
        neg.append(((word_feats(pptweet)),'neg'))
    elif(int(senti)==4):
        pptweet = preprocess(text)
        pos.append(((word_feats(temp)),'pos'))
    if(i>1000):
            break

print(neg[:5])
print(pos[:5])