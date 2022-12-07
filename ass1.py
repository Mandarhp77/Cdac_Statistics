import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Housing.csv")
df.head()


# 1
df['price'].skew()

df['price'].kurtosis()

df['price'].plot(kind='hist',bins=25)

# 2
sns.scatterplot(data=df,x='lotsize',y='price',hue='airco')

#3

sns.boxplot(data=df, y='price',x='bathrms')

#4
plt.subplot(2,2,1)
sns.boxplot(data=df, y='price')
plt.title('boxplot')

plt.subplot(2,2,2)
sns.histplot(data=df, x='price')
plt.title('histplot')

plt.subplot(2,2,3)
sns.scatterplot(data=df,x='lotsize', y='price',hue='bathrms')
plt.title('scatterplot')

plt.subplot(2,2,4)
bar = df['bathrms'].value_counts()
bar.plot(kind='bar')
plt.title('barplot')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

#5
a=sns.FacetGrid(data=df, col='bathrms')
a=a.map(plt.scatter, 'lotsize', 'price')
plt.show()

a=sns.FacetGrid(data=df, row='bathrms')
a=a.map(plt.scatter, 'lotsize', 'price')
plt.show()

#6
sns.jointplot(data=df, x='lotsize', y='price')


