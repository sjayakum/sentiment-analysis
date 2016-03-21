# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:16:48 2016

@author: suraj
"""


from nltk.tokenize import TweetTokenizer,sent_tokenize
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
from nltk import pos_tag
import re


def preprocess(sentence):
    output_list = []
    
    #CASE FOLDING [NOT COMPLETE]
    sentence = sentence.lower()
    
    #DATA CLEANING
    sentence = sentence.replace('[https://]?[t.co/]?','')
    sentence = sentence.replace('[#]?','')
    sentence = sentence.replace('[RT]?','')
    sentence = sentence.replace(',','')
    sentence= sentence.replace('!','')
    sentence= sentence.replace('?','')
    sentence= sentence.replace('.','')
    sentence= sentence.replace('\'','')
    sentence= sentence.replace('\"','')
    sentence= sentence.replace(':','')
    #REMOVE REPEATED CHARS
    sentence = re.sub(r'(\w)\1+', r'\1', sentence)
    
    #TOKENIZE
    tt = TweetTokenizer()
    temp = tt.tokenize(sentence)
    
    #REMOVE STOP WORDS
    stop = stopwords.words('english')
    
    #STEMMING 
    ls = LancasterStemmer()
    newtemp = [eachword for eachword in temp if eachword not in stop]
    for eachword in newtemp:
        output_list.append(ls.stem(eachword))
    
    return output_list
    

        
print preprocess("@remy: This is waaaaayyyy too much for you!!!!!!")
        
        
    