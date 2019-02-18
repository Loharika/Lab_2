import numpy as np
import matplotlib.pyplot as plt
Fs = 8000
f = 5
sample=5000
x = np.arange(sample)
y2 = np.sin((2 * np.pi * f * x / Fs))
y1 = np.sin((2 * np.pi * f * x / Fs)+180)
y = y1+y2
plt.subplot(131)
plt.plot(x,y1,'g')
plt.subplot(132)
plt.plot(x,y2,'b')
plt.subplot(133)
plt.plot(x,y,'k')
plt.xlabel('Fs')
plt.ylabel('voltage')
plt.show()

