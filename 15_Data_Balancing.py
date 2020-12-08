import pandas as pd
df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/spam.csv',encoding='latin-1')
df.head()

df['v1'].value_counts()

# Data balancing
ham = df[df['v1'] == 'ham']
spam = df[df['v1'] == 'spam']

ham
spam

ham = ham[:747]

df = pd.concat([ham, spam])
df

df1 = df.sample(frac=1).reset_index(drop=True)
df1

df1.to_csv('/Users/Admin/Documents/Python/machine_learning/balanced_spam.csv')
