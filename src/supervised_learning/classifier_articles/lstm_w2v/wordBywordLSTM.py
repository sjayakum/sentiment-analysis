import pickle
from nltk.corpus import movie_reviews
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential, model_from_json
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.datasets import imdb
from gensim.models import Word2Vec,Doc2Vec
model2 = Doc2Vec.load_word2vec_format('full_corpus.vec')

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')


model = Sequential()
model.add(LSTM(100,batch_input_shape=(1,1,100)))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam')
X_train = []
y_train = []
X_test = []
y_test = []
for i in negids[:-20]:
    X_train.append(np.reshape( np.sum(model2[movie_reviews.words(i)],axis=0)/model2[movie_reviews.words(i)].shape[0] ,(1,100)))
    y_train.append(0)

for i in posids[:-20]:
    X_train.append(np.reshape( np.sum(model2[movie_reviews.words(i)],axis=0)/model2[movie_reviews.words(i)].shape[0] ,(1,100)))
    y_train.append(1)

for i in negids[-20:]:
    X_test.append(np.reshape( np.sum(model2[movie_reviews.words(i)],axis=0)/model2[movie_reviews.words(i)].shape[0] ,(1,100)))
    y_test.append(0)

for i in posids[-20:]:
    X_test.append(np.reshape( np.sum(model2[movie_reviews.words(i)],axis=0)/model2[movie_reviews.words(i)].shape[0] ,(1,100)))
    y_test.append(1)
    

    
model.fit(np.array(X_train), np.array(y_train), batch_size=1, nb_epoch=100,show_accuracy=True)
score, acc = model.evaluate(np.array(X_test), np.array(y_test),
                            batch_size=1,
                            show_accuracy=True)
                            
open('lstm_sa.json','w').write(model.to_json())
model.save_weights('lstm_sa.h5',overwrite=True)

model = model_from_json(open('lstm_sa.json').read())
model.load_weights('lstm_sa.h5')
                            
                            
print('Test score:', score)
print('Test accuracy:', acc)
print len(X_train)
print len(y_train)
print X_train[0].shape

print y_test
mycounter = 0
for i in range(40):
    output = model.predict(np.array([X_test[i]]),batch_size=1)
    if(output[0][0]>0.5):
        #print 1,y_test[i]
        if (y_test[i]==1):
            #print "CORRECT"
            mycounter += 1

            #print "WRONG"
    else:
        #print 0,y_test[i]
        if (y_test[i]==0):
            #print "CORRECT"
            mycounter+=1
            
            
print mycounter
        

