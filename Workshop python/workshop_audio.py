import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

data, rate = sf.read('sample.wav')
n=10*rate
print(rate)
m = data.shape
if len(m)==2:
 data3 = data[:,0]
else:
 data3 = data.copy()

del data
data = np.zeros((m[0], 2))
data[:, 0] = data3
data[:, 1] = data3

data2 = np.zeros(data.shape)
for i in range(0, m[0]):
    if (i % n < n / 2):
        data2[i][1] = data[i][1] * (i % (n / 2)) / (n / 2)
        data2[i][0] = data[i][0] * ((n - i) % (n / 2)) / (n / 2)
    else:
        data2[i][0] = data[i][0] * (i % (n / 2)) / (n / 2)
        data2[i][1] = data[i][1] * ((n - i) % (n / 2)) / (n / 2)

sf.write('sample8D.wav',data2,rate)

plt.figure(1)
n1=np.arange(0,20,1)
yd0=data[np.arange(0,8000*5,2000),0]
yd20=data2[np.arange(0,8000*5,2000),0]
yd1=data[np.arange(0,8000*5,2000),1]
yd21=data2[np.arange(0,8000*5,2000),1]
plt.subplot(221)
plt.ylim([-0.1, .5])
plt.stem(n1,yd0,use_line_collection=True)
plt.subplot(222)
plt.ylim([-0.1, .5])
plt.stem(n1,yd20,use_line_collection=True)
plt.subplot(223)
plt.ylim([-0.1, .5])
plt.stem(n1,yd1,use_line_collection=True)
plt.subplot(224)
plt.ylim([-0.1, .5])
plt.stem(n1,yd21,use_line_collection=True)

y2d0=data[np.arange(8000*5,8000*10,2000),0]
y2d20=data2[np.arange(8000*5,8000*10,2000),0]
y2d1=data[np.arange(8000*5,8000*10,2000),1]
y2d21=data2[np.arange(8000*5,8000*10,2000),1]

plt.figure(2)
plt.subplot(221)
plt.ylim([-0.2, .2])
plt.stem(n1,y2d0,use_line_collection=True)
plt.subplot(222)
plt.ylim([-0.2, .2])
plt.stem(n1,y2d20,use_line_collection=True)
plt.subplot(223)
plt.ylim([-0.2, .2])
plt.stem(n1,y2d1,use_line_collection=True)
plt.subplot(224)
plt.ylim([-0.2, .2])
plt.stem(n1,y2d21,use_line_collection=True)
plt.show()