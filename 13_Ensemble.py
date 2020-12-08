import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/spam.csv',encoding='latin-1')
df.head()

df = df[['v1','v2']]
df = df.rename(columns={'v1': 'class','v2': 'text'}) # change column name
df.head()

x = df ['text']
y = df['class']

# divide train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
x_train
y_train

# แปลง text ให้เป็นตัวเลข
vectorizer = CountVectorizer()
vectorizer = vectorizer.fit(x)
vectorizer_text = vectorizer.transform(x_train)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(vectorizer_text,y_train)

from sklearn.metrics import accuracy_score
vectorizer_text_test = vectorizer.transform(x_test)
y_pred = model.predict(vectorizer_text_test)

accuracy_score(y_test , y_pred)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred, labels=['ham', 'spam'])

