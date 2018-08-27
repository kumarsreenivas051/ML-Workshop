import matplotlib.pyplot as plt
x1=[0,2,0]
y1=[0,4,3]
plt.plot(x1,y1,label="line 1")
x2=[3,1,4]
y2=[5,3,1]
plt.plot(x2,y2,label="line2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('First plot')
plt.legend()
plt.show()
