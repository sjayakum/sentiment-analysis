import numpy as np
import matplotlib.pyplot as plt


N = 24
positive = (350,250,390,600)
negative =(200,150,400,200)
ind = np.array([1,2,3,4])    # the x locations for the groups
width = 0.25       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, positive, width, color='#00e500')
p2 = plt.bar(ind, negative, width, color='r',
             bottom=positive)

plt.ylabel('Tweets [Pos/Neg]')
plt.xlabel('Celebrity')
plt.title('Tweets vs Celebs')
my_xticks = ['Abhijeet','Rajdeep','Swamy','Anupam Kher']
plt.xticks(ind, my_xticks)
plt.legend((p1[0], p2[0]), ('Positive', 'Negative'))

plt.show()