# Generated from: Decision Tree.ipynb
# Converted at: 2026-04-20T10:21:42.844Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import  DecisionTreeClassifier

iris = load_iris()

df = pd.DataFrame(iris.data,columns = iris.feature_names)

df.head()

df.tail()

df.describe()

df.isnull().sum()

df.columns

df['species']= iris.target

x = df.drop(columns = 'species')

y = df['species']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.2,random_state = 42)

model = DecisionTreeClassifier(max_depth = 6)


model.fit(x_train,y_train)

pred = model.predict(x_test)

acc = accuracy_score(y_test,pred)

acc*100

imp = model.feature_importances_

imp

x

plt.barh(x.columns,imp)
plt.title('Horizontal bar grph wrt feature selection')
plt.show()

from sklearn.tree import plot_tree

plt.figure(figsize = (10,6))
plot_tree (model,feature_names = iris.feature_names,class_names = iris.target_names,filled = True,rounded = True)
plt.show()

df = pd.read_csv(r'https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv')

df.head()

df.tail()

df.describe()

df.isnull().sum()

x = df.drop(columns = ['Outcome'])
y = df['Outcome']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.2,random_state = 42)

x_train

model = DecisionTreeClassifier(max_depth = 3)


model.fit(x_train,y_train)

pred = model.predict(x_test)

pred

acc = accuracy_score(y_test,pred)

acc*100

imp = model.feature_importances_

imp

x

plt.barh(x.columns,imp)
plt.title('Horizontal bar graph for important features')
plt.show

plt.figure(figsize = (12,6))
plot_tree (model,feature_names = x.columns,class_names = ['diabetic','non-diabetic'],filled = True,rounded = True)
plt.show()

df1 = pd.read_csv(r"C:\Users\Pradip\Downloads\Netflix Shows.csv",encoding = 'latin-1')

df1.head()

df1.tail()

df1.describe()

df1.info()

df1.isnull().sum()

df1.columns

df1['ratingLevel'] = df1['ratingLevel'].fillna(df1['ratingLevel'].mode()[0])

df1['user rating score'] = df1['user rating score'].fillna(df1['user rating score'].mean())

df1.isnull().sum()

df1 = df1.drop(columns = ['rating', 'ratingLevel'])

df1

df1 = df1.drop(columns = ['ratingDescription'])

df1

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df1['title'] = le.fit_transform(df1['title'])

df1

df1.info()

X1 = df1.drop(columns = ['user rating score'])

y1 = df1['user rating score']

from sklearn.tree import DecisionTreeRegressor

X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,test_size =0.2,random_state =42)

model1 = DecisionTreeRegressor(max_depth=3)

model1.fit(X1_train,y1_train)

y1_pred = model1.predict(X1_test)

y1_pred

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y1_test,y1_pred)

mae

imps = model1.feature_importances_

imps

plt.figure(figsize=(10,5))
plot_tree(model1,feature_names = X1.columns,filled = True,rounded=True)
plt.show()