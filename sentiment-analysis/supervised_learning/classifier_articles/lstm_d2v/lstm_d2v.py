# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:53:29 2016

@author: suraj
"""
# gensim modules

from gensim.models import Doc2Vec

# np
import numpy as np
from keras.layers.core import Dense, Dropout, Activation
from keras.models import Sequential, model_from_json
from keras.layers.recurrent import LSTM


# classifier
from sklearn.linear_model import LogisticRegression


model2 = Doc2Vec.load('./imdb.d2v')

model2.most_similar('good')
train_arrays = np.zeros((25000,1, 100))
train_labels = np.zeros(25000)

for i in range(12500):
    prefix_train_pos = 'TRAIN_POS_' + str(i)
    prefix_train_neg = 'TRAIN_NEG_' + str(i)
    train_arrays[i][0] = model2.docvecs[i]
    train_arrays[12500 + i] [0]= model2.docvecs[i+12500]
    train_labels[i] = 1
    train_labels[12500 + i] = 0
    test_arrays = np.zeros((25000,1, 100))
test_labels = np.zeros(25000)

for i in range(12500):
    prefix_test_pos = 'TEST_POS_' + str(i)
    prefix_test_neg = 'TEST_NEG_' + str(i)
    test_arrays[i][0] = model2.docvecs[25000+i]
    test_arrays[12500 + i][0] = model2.docvecs[25000+12500+i]
    test_labels[i] = 1
    test_labels[12500 + i] = 0

'''
model = Sequential()
model.add(LSTM(100,batch_input_shape=(1,1,100)))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam')
              
              

model.fit(train_arrays, train_labels, batch_size=1, nb_epoch=10,show_accuracy=True)
score, acc = model.evaluate(np.array(test_arrays), np.array(test_labels),
                            batch_size=1,
                            show_accuracy=True)
                            

print('Test score:', score)
print('Test accuracy:', acc)

open('lstm_new.json','w').write(model.to_json())
model.save_weights('lstm_new.h5',overwrite=True)
'''

model = model_from_json(open('lstm_new.json').read())
model.load_weights('lstm_new.h5')

#
#score, acc = model.evaluate(np.array(test_arrays), np.array(test_labels),
#                            batch_size=1,
#                            show_accuracy=True)
#                            
#
#print('Test score:', score)
#print('Test accuracy:', acc)
#
#
#
#test_str = "this is  a stupid  film really pointless and bad"
#mytemp =np.reshape( np.sum( model2[test_str.split()],axis=0)/len(test_str.split()) ,(1,100))
#
#output = model.predict(np.array([mytemp]))
#print output[0][0]
#
#if(output[0][0]>0.5):
#    print "Positive"
#else:
#    print "Negative"

print model.predict(np.array([test_arrays[0]]))
print model.predict(np.array([test_arrays[-1]]))