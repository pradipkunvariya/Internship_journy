# Generated from: Unsupervised Learning.ipynb
# Converted at: 2026-04-20T10:21:31.214Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Polynomial Regression


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import  DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier

x = [[1],[2],[3],[4]]
y = [1,4,9,16]

p = PolynomialFeatures(degree=2)

x_p = p.fit_transform(x,y)

x_p

model = LinearRegression()

model.fit(x_p,y)

p1 = model.predict(p.fit_transform([[5]]))

p1

plt.scatter(x,y,marker='d',s =300,color='red')
plt.show

# # unsupervised learning


x1=np.array([[1,2],[2,0],[2,2],[8,9],[9,8],[9,9]])

model = KMeans(n_clusters = 2)

model.fit(x1)

labels= model.predict(x1)

labels

plt.scatter(x1[:,0],x1[:,1])
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s = 550)
plt.show()