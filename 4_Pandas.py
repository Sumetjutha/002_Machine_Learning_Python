# Import library
import pandas as pd

# read_csv
df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/running.csv')

# check head datas
df.head()
df.head(10)

# check tail datas
df.tail(4)

# check shapes datas
df.shapes

# check size datas
df.size

# check columns datas
df.columns
# call to watch column sick , or other
df['sick?']
df['stadium close']  # using copy and paste

df[['go out?','is raining','sick?']]

## if else in data frame
df[df['is raining'] == 'Y']

