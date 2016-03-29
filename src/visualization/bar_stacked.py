import numpy as np
import matplotlib.pyplot as plt


N = 24
positive = (2,3,4,1,20, 35, 30, 35, 27,45,54,60,65,70,55,50,65,50,40,30,25,16,9,3)
negative = (1,4,2,3,25, 32, 34, 20, 25,35,27,45,40,25,20,35,20,10,25,10,7,5,4,1)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, positive, width, color='#00e500')
p2 = plt.bar(ind, negative, width, color='r',
             bottom=positive)

plt.ylabel('Tweets')
plt.xlabel('Hour of the Day')
plt.title('Tweets per hour')
plt.xticks(ind + width/2., np.arange(24)+1)
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Positive', 'Negative'))

plt.show()