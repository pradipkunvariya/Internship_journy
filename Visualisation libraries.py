# Generated from: Visualisation libraries.ipynb
# Converted at: 2026-04-20T10:21:58.512Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import plotly.express as px

# # Visualisation Libraries 
# 
# #### -> We need visualising libraries to make our data look effective by extracting the useful insughts from them.
# #### -> Three main libraries will be in action here:
# 
# #### 1) Matplotlib - For matrix visuals and considered as the most basic and useful visualising library.
# #### 2) Seaborn ->  Highly utilized to check correlation matrix, also it adds more
# #### filters to the graphs(visuals).
# 
# #### 3)Plotly / Plotly express -> Most advance visualising tool, when it comes
# #### to plot graphs in the most appropriate way.


import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

a = [5,10,15,20,25]
b = [200,250,300,350,400]

# ## Line plot :
# 
# ### -> For trend analysis.
# ### -> Mainly for seasonal trend analysis.
# 
# ### -> Eg: Sales of an electronic store during summer season, stock market prices.


# # Line plot


plt.plot(a,b,color = 'blue',linestyle = '--',linewidth = 2)
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.grid()
plt.show()

# # Line plot through seaborn


sns.lineplot(x=a,y=b)
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.grid()
plt.show()

# # Lineplot through plotly


px.line(x=a,y=b).show()

# # Bar plot
# 
# ### -> Utilized to see frequency of values given
# ### -> Best known for comparison between values.


plt.bar(a,b,color = ['red','yellow','green','blue'])
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.grid()
plt.show()


# # Horizontal bar plot


plt.barh(a,b,color = ['red','yellow','green','blue'])
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.show()


# # Bar plot through seaborn


sns.barplot(x=a,y=b)
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.show()


# # Bar plot through plotly
# 


px.bar(x=a,y=b).show()

# # Scatter Plot:
# ### When there is a need to find a distance between the given data points,the scatter points is used .
# ### It helps us to understand how data points are nearer/far awayfrom each other


plt.scatter(a,b,marker='D',s=300,color='red')
plt.title('Performance')
plt.xlabel('marks got')
plt.ylabel('to be achieved')
plt.grid()
plt.gca().set_facecolor('yellow')
plt.gcf().set_facecolor('lightblue')

plt.show()

# # Scatter plot through seaborn


sns.scatterplot(x=a,y=b,marker='D',s=300,color = 'green')
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.gca().set_facecolor('yellow')
plt.gcf().set_facecolor('lightblue')
plt.grid()
plt.show()

# # Scatter plot through plotly


fig1 = px.scatter(x=a,y=b)
fig1.update_layout(plot_bgcolor = 'yellow',paper_bgcolor = 'green')

df = sns.load_dataset('iris')

df

corr = df.corr(numeric_only=True)

corr

# # Heatmap 


sns.heatmap(corr,annot = True,cmap = 'magma')
plt.xlabel('')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.show()

fig3 = px.imshow(corr,text_auto = True,color_continuous_scale = 'magma')
fig3.update_layout(plot_bgcolor = 'Blue',paper_bgcolor = 'yellow')
plt.show()

# # Pairplot


sns.pairplot(df)
plt.show()

# # Pie chart:
# ### -> Distribution is done her in the percentage format.
# ### -> Sales amount per year,marks obtained by acandidate can be best displayed through pie chart.


marks = [80,90,95,85,66]
Subjects = ['maths','Science','Physics','Chemistry','Data science']

plt.pie(sizes,labels=labels,autopct = '%1.3f%%')
plt.title('Performance')
plt.gcf().set_facecolor('lightblue')
plt.show()

px.pie(names = Subjects,values = marks,hole = 0.5).show()

A = [2,5,6,9,8,4,1]
B = [200,300,600,800,400,900,250]

# # Step plot


plt.step(A,B)
plt.title('Performance')
plt.gcf().set_facecolor('lightblue')
plt.show()

# # Stem plot


plt.stem(A,B)
plt.title('Performance')
plt.gcf().set_facecolor('lightblue')
plt.show()

import numpy as np

n = np.random.rand(100)

n

# # Histplot


plt.hist(n,bins = 20)
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.show()

# # Histplot through seaborn


sns.histplot(n,bins = 20,kde = True)
plt.xlabel('marks')
plt.ylabel('to be achieved')
plt.title('Performance')
plt.show()

# # Histplot through plotly


px.histogram(n,nbins = 20,opacity=0.8,title = 'Histogram using px')

# # Boxplot


plt.boxplot(n)
plt.show()

n1 = [1,2,3,4,100000]

plt.boxplot(n1)
plt.show()

# # Boxplot through seaborn 


sns.boxplot(n)
plt.show()

# # Box plot through plotly


px.box(n).show()

# # Violine plot


# ### Commute time calculation.
# ### Time taken to travel from source to destination.


plt.violinplot(n)
plt.show()

# # Violin plot through seaborn


sns.violinplot(n)
plt.show()

# # violin plot through plotly


px.violin(n)