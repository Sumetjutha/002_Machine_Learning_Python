import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,5,6,7,9]

plt.scatter(x,y)
plt.show()

plt.plot(x,y)
plt.show()

import random
ages = [random.randrange(1,100) for i in range(1000)]
print(ages)

plt.hist(ages, bins=10,color='salmon') 
plt.show()
# cyan
# r g b c m

plt.xlabel('ages')
plt.ylabel('number')

plt.hist(ages,bins=10,color='c')
plt.show()

values = [2,3,4,5,8]

plt.bar(['a','b','c','d','e'],values,color='salmon')
plt.show()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs','Cats'
sizes = [15, 30, 25, 10, 20]
explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
