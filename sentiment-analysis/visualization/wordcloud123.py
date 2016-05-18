#import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud


f1 = open("rajdeep.txt",'r')
f2 = open("test.txt",'w')

def preprocess(sentence):
    #CASE FOLDING [NOT COMPLETE]
    sentence = sentence.lower()

    #DATA CLEANING
    sentence = sentence.replace('https','')
    sentence = sentence.replace('t.co','')
    sentence = sentence.replace('sardesairajdeep','')
    sentence = sentence.replace('abhijtmajumder','')
    sentence = sentence.replace('anupamPkher','')
    sentence = sentence.replace('@','')
    sentence = sentence.replace('[#]?','')
    sentence = sentence.replace('rt','')
    sentence = sentence.replace(',','')
    sentence = sentence.replace('!','')
    sentence = sentence.replace('?','')
    sentence = sentence.replace('.','')
    sentence = sentence.replace('\'','')
    sentence = sentence.replace('\"','')
    sentence = sentence.replace(':','')
    sentence = sentence.replace('indiatoday','')
    sentence = sentence.replace('today','')
    sentence = sentence.replace('new','')
    #REMOVE REPEATED CHARS
    #sentence = re.sub(r'(\w)\1+', r'\1', sentence)

    return sentence

for eachline in f1:
    f2.write(preprocess(eachline))
f2.close()
f1.close()
# Read the whole text.
text = open('test.txt').read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
#alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

wc = WordCloud(background_color="white", max_words=2000)
# generate word cloud
wc.generate(text)


# store to file
#wc.to_file(path.join(d, "alice.png"))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
#plt.imshow(alice_mask, cmap=plt.cm.gray)
#plt.axis("off")
plt.show()