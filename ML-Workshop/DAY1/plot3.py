import matplotlib.pyplot as plt

left=[3,4,5,6,7]

heights=[10,24,36,42,30]

tick_label=['one','two','three','four','five']
plt.bar(left,heights,tick_label=tick_label,width=0.8,color=['red','blue'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My bar graph!')
plt.show()
