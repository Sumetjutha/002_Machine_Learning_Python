import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/kc_house_data_2.csv')
df.head()

x = df['price']
y = df['sqft_living']

plt.scatter(x,y)
plt.show()

from scipy import stats
line = stats.linregress(x,y)

line

def predict(x):
      # y = ax + b
  return line.slope * x + line.intercept

predict(4.74)

y_predict = predict(x)

plt.plot(x, y_predict, c='r')
plt.scatter(x,y)
plt.show()