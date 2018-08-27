import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,3,1,4,2,6]
plt.plot(x,y,color='green', linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)

plt.ylim(1,7)
plt.xlim(1,7)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Custom Config')
plt.show()
