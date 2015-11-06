import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from random import randint 
import time
#import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):  
    m = open('twitScores.txt','r')
    pullData = m.read()
    m.close()
    dataArray = pullData.split('\n')
    
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.set_ylim([0,4])
    ax1.set_title("LIVE TWEET FEED")
    ax1.set_ylabel("Sentiment Value")
    ax1.set_xlabel("Tweet Number")
    line_up, = plt.plot([], label='Line 2')
    line_down, = plt.plot([], label='Line 1')
    plt.legend([line_up, line_down], ['1-Bad', '2-Good'])
    #ax1.set_yticklabels(('','','Bad','Good','',''))
    ax1.plot(xar,yar)
    #print(i) 


ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()