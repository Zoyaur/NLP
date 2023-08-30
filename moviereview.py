# -*- coding: utf-8 -*-
"""moviereview.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yQnox4UavZxJMByf5mGdwO1__NyRYGDE
"""



from google.colab import drive
drive.mount('/content/drive')

"""# New Section"""

!pip install scikit-learn

import numpy as np
import pandas as pd
df=pd.read_csv('moviereviews.tsv',sep='\t')
df.head()

len(df)



df.isnull().sum()

newdf = df.dropna()

newdf.isnull().sum()

newdf['label'].unique()

newdf['label'].value_counts()

print(983/(983+982))

x=newdf['review']
y=newdf['label']

"""email can be categorized by four column like label:spam,ham msg , lenght , pucntuation"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.33,random_state=10)


print('training data:' , x_train.shape)
print('Test data:',x_test.shape)

x_train.head()

y_train.head()

"""70% testing 30% training"""

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()

x_train_counts = count_vect.fit_transform(x_train)

x_train_counts.shape

tempdf = pd.DataFrame(x_train_counts)
tempdf.head()