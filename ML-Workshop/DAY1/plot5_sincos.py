import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2*(np.pi),0.1)
y1=np.cos(x)
y2=np.sin(x)

plt.plot(x,y1,label="cos")
plt.plot(x,y2,label="sin")
plt.legend()
plt.show()
