import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10]

y=[2,3,5,6,7,9,12,13,14,15]

plt.scatter(x,y,label="stars",color="red",marker="*",s=30)

plt.xlabel('x-axis')

plt.ylabel('y-axis')

plt.title('Scatter plot')

plt.legend()
plt.show()
