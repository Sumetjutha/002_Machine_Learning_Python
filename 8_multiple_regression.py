import pandas as pd

df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/kc_house_data_2.csv')
df.head()

df.columns

y = df['price']
x = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement']]
x.head()

import statsmodels.api as sm

model = sm.OLS(y,x).fit()

model.summary()

model.predict([3,	1.00,	1180,	5650,	1.0,	0,	0,	3,	7,	1180,	0])

y.head()

test_data = x.iloc[2]
test_data = test_data.values
print(test_data)

model.predict(test_data)
