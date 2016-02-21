import pickle

classiifer = pickle.load(open('NaiveBayesClassifierNLTK.pickle','rb'))


sentence = "Great this is really good"
def word_feats(words):
    """
    :param words: takes any english sentence
    :return: a dictionary by splitting each word in the sentence where 'word' is the key and 'True' is the value
    """
    return dict([(word, True) for word in words])

def TestData1():
    fobj = open(r'E:\Capstone Project\capstoneproject\src\chatDataClassifier\trainingData\testingSet\testdata1_unclassified.txt')
    for eachline in fobj:
        print eachline,classiifer.classify(word_feats(eachline))

print classiifer.classify(word_feats(sentence))
