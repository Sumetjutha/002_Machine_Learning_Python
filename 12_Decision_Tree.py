import pandas as pd

df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/running.csv')
df.head()

# Mapping ให้อยู่ในรูปตัวเลข
d = {'Y':1, 'N':0}
df.columns

df['go out?'] = df['go out?'].map(d)
df['is raining'] = df['is raining'].map(d)
df['is hot'] = df['is hot'].map(d)
df['sick?'] = df['sick?'].map(d)
df['work'] = df['work'].map(d)
df['stadium close'] = df['stadium close'].map(d)

df.head()


# set train and test model
from sklearn.tree import DecisionTreeClassifier
y = df['go out?']
x = df[['is raining', 'is hot', 'sick?', 'work', 'stadium close','last time go out(day)']]

model = DecisionTreeClassifier()
model = model.fit(x, y)

# Create chart decision tree
from IPython.display import Image
from six import StringIO
from sklearn import tree
import pydotplus
import graphviz

dot_data = StringIO()
tree.export_graphviz(model, out_file=dot_data,feature_names=['is raining', 'is hot', 'sick?', 'work', 'stadium close','last time go out(day)'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph

# predict
model.predict([[0, 1, 0, 0, 0, 3]])

from six import StringIO
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()

