import pandas as pd

df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/bitcoin.csv')

df.head()

df.shape

x = [i for i in range(1877)]
y = df['Adj Close']

x

y

import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.show()

import numpy as np

model = np.poly1d(np.polyfit(x,y,11))

model(500)

plt.scatter(x,y)
plt.plot(x,model(x),c='r')

plt.show()
