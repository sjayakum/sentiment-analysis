from gensim.models import Word2Vec
import numpy as np
# sentences = [ ['first', 'sentence'],['second','sentence']]
# model = Word2Vec(sentences=sentences,min_count=1)
#
#
# print model['first']
# print np.array(model['first']).shape


def word2vec(document):
    """
    :param document: It is a list of tokenized sentences
                    Example : [ ['first', 'sentence'],['second','sentence']]
    :return:
    """
    model = Word2Vec(sentences=document,min_count=1)
    return model
