from gensim.models import Word2Vec,Doc2Vec
from nltk.corpus import movie_reviews
import pickle

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')


def word2vec(document):
    """
    :param document: It is a list of tokenized sentences
                    Example : [ ['first', 'sentence'],['second','sentence']]
    :return:
    """
    model = Word2Vec(sentences=document,min_count=1)
    return model


full_corpus = []

for i in negids:
    full_corpus.extend(movie_reviews.sents(i))

for i in posids:
    full_corpus.extend((movie_reviews.sents(i)))

print len(full_corpus)

print full_corpus[0]

print full_corpus[1]

print full_corpus[0][0]

model = word2vec(full_corpus)
print model['bad']
print model['good']
#pickle.dump(model,open('full_corpus_w2v.p','wb'))
model2 = Doc2Vec.load_word2vec_format('full_corpus_w2v.p')
model2['i love this so much']