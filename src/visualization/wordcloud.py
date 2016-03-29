#import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud



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