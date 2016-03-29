import pickle
from nltk.classify import NaiveBayesClassifier
test_article = """
ith the debate on nationalism coming to the fore, the BJP on Sunday said freedom of expression does not give a right to seek the country's destruction, as the issue found the pride of place in the political resolution adopted at its national executive meeting here.
The issue of nationalism continued to take the centrestage in the deliberations at the two-day meet after party chief Amit Shah set the tone in his inaugural address on Saturday saying the BJP will not tolerate any attack on the nation.
"Freedom of expression and nationalism do necessarily coexist" and the Constitution gives full freedom for expressing dissent and disagreement, but not the country's destruction, Union minister Arun Jaitley said while briefing reporters on the meeting.
"The ideology of nationalism guides our beliefs and philosophy," he asserted as the meeting saw the dominant mood among party leaders to put the Congress on the mat over the recent JNU-related developments.
Asked whether the executive also discussed the row over the slogan 'Bharat mata ki jai', Jaitley said the party believes it is an issue over which there should be no debate.
People have no problem with this slogan and "we saw this in Kolkata yesterday", he said as he sought to buttress his point by referring to the spectators raising the slogan after India's win in the cricket match with Pakistan.
The finance minister, a key party strategist, also targeted Congress over its political strength, saying the main opposition party had "lowered" its stature and was "content to be a tail-ender of any alliance" in states like Bihar, West Bengal and Tamil Nadu.
Though issues of government formation in Uttarakhand where Congress government is facing a rebellion in its ranks, and Jammu & Kashmir did not come up for discussion at the meeting, Jaitley said the resolution emphasized the party's commitment to the 'agenda of governance' in J&K.
Talks between BJP and PDP to revive their coalition government in J & K have fallen through but the saffron party has insisted that its doors are not shut on its former partner which will however have to stop putting more conditions.

"""

#every word before feeding in to NaiveBayes Classifier should be of this form
def word_feats(words):
    """
    :param words: takes any english sentence
    :return: a dictionary by splitting each word in the sentence where 'word' is the key and 'True' is the value
    """
    return dict([(word, True) for word in words])


classifier = pickle.load(open('NaiveBayesGood.p'))

print classifier.classify(word_feats(test_article))