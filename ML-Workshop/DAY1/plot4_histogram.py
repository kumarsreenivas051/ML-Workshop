import matplotlib.pyplot as plt
ages=[2,5,3,10,22,21,76,44,39,27,82,11,42,13,54,34,20,16,63,68,67,69,90,97,94,95]

range=(0,100)
bins=10
plt.hist(ages,bins,range,color='yellow',histtype='bar',rwidth=0.8)
plt.xlabel('age')

plt.ylabel('No. of people')
plt.title('Histogram')
plt.show()
