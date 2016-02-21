from keras.models import  Sequential
from keras.layers import LSTM
from keras.layers.core import Dense, Dropout
from keras.layers import  Embedding
from keras.optimizers import  RMSprop
from keras.layers import  Activation


#CREATE DATA
#Note: The dim of each line will be 100 word2vec
#maximum features for each tweet -> 100


embedding_size = 64
max_features = 100
X=0
y=0
batch_size =0
nb_epoch = 0
model = Sequential()
model.add(Embedding(max_features,embedding_size))
model.add(LSTM(embedding_size,64))
model.add(Dense(64,1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')



model.fit(X,y,batch_size=batch_size,nb_epoch=nb_epoch,verbose=1)

