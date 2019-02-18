import numpy as np
import matplotlib.pyplot as plt
Fs1 = 100
f1 = 05
sample = 100
x = np.arange(sample)
y1 = np.sin(2 * np.pi * f1 * x / Fs1)
plt.subplot(311)
plt.plot(x,y1,'g')
plt.xlabel('sample(n)')
plt.ylabel('sample(V)')
Fs2 = 400
f2 = 10
sample = 100
x = np.arange(sample)
y2 = np.sin(2 * np.pi * f2 * x / Fs2)
plt.subplot(312)
plt.plot(x,y2,'b')
plt.xlabel('sample(n)')
plt.ylabel('sample(V)')
z=y1+y2
plt.subplot(313)
plt.plot(x,z,'k')
plt.xlabel('sample(n)')
plt.ylabel('sample(V)')
plt.show()
