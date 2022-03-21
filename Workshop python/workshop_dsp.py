import numpy as np
import matplotlib.pyplot as plt


n1= np.array([1,2,3,4])
x1= np.array([4,3,2,1])
x2= np.array([-1, -3, -5, -2])
y1 = x1+x2
y2 = x1-x2
y3 = x1*x2
y4 = x1/x2

plt.figure(1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sample Data')

plt.plot(n1,x1,'g^')
plt.plot(n1,x2,'r--')
plt.xlim([0,5])
plt.ylim([-6,5])

plt.show()



plt.figure(2)
plt.subplot(321)
plt.ylabel('X1')
plt.stem(n1,x1, use_line_collection=True)
plt.subplot(322)
plt.ylabel('X2')
plt.stem(n1,x2, use_line_collection=True)
plt.subplot(323)
plt.ylabel('X1+X2')
plt.stem(n1,y1, use_line_collection=True)
plt.subplot(324)
plt.xlabel('n1')
plt.ylabel('X1-X2')
plt.stem(n1,y2, use_line_collection=True)
plt.subplot(325)
plt.xlabel('n1')
plt.ylabel('X1*X2')
plt.stem(n1,y3, use_line_collection=True)


plt.subplot(326)
plt.ylabel('X1/X2')
plt.stem(n1,y4, use_line_collection=True)

plt.show()

plt.figure(3)

plt.subplot(321)
plt.ylabel('X1')
plt.plot(n1,x1)
plt.show(block=False)
plt.pause(1)

plt.subplot(322)
plt.ylabel('X2')
plt.plot(n1,x2)
plt.show(block=False)
plt.pause(1)

plt.subplot(323)
plt.ylabel('X1+X2')
plt.plot(n1,y1)
plt.show(block=False)
plt.pause(1)


#plt.subplot(324)
#plt.ylabel('X1-X2')
#plt.plot(n1,y2)

'''
plt.subplot(325)
plt.xlabel('n1')
plt.ylabel('X1*X2')
plt.plot(n1,y3)
'''

plt.subplot(326)
plt.xlabel('n1')
plt.ylabel('X1/X2')
plt.xlim([0,5])
plt.ylim([-4,0])
for i in range(len(n1)):
    plt.plot(n1[0:i+1], y4[0:i+1])
    plt.show(block=False)
    plt.pause(1)
plt.show()

