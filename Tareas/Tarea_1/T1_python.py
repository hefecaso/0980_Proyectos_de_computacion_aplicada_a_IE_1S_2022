import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2,0.01)*2*np.pi
y = np.sinh(x)

plt.axis([0, 7,-1,1])
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
