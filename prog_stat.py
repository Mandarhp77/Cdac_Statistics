import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


cars93 = pd.read_csv("Cars93.csv")


print(cars93.shape)
print(cars93.columns)
print(cars93.dtypes)
print(cars93.info())


cars93['Price'].mean()
cars93['Price'].median()
cars93['Price'].quantile(q=0.25)
cars93['Price'].quantile(q=0.75)
cars93['Price'].quantile(q=1)


cars93['Price'].quantile(q=np.array([0,0.25,0.5,0.75,1]))
cars93['Price'].plot(kind='box')
cars93['Price'].plot(kind='line')
cars93['Price'].plot(kind='hist', bins =25)
plt.show()

cars93['Price'].skew()

cars93['Price'].kurtosis()


cts=cars93['AirBags'].value_counts()
cts.plot(kind='hist',bins = 15)
cts


plt.bar(cts.index,cts)
plt.show()


cts1=cts.reset_index()
cts1.columns =('Type','Count')
sns.barplot(data=cts1,y='Type',x='Count')
plt.show()

sns.histplot(data=cars93, x='Price', bins=25)

cars93['AirBags'].skew()

sns.scatterplot(data=cars93, x='EngineSize', y='MPG.highway',hue='AirBags')

cars93.describe()

cars93['Price'].plot(kind='box')


plt.boxplot(cars93["Price"])
plt.title("Box Plot")

plt.boxplot(cars93["Price"])
plt.title("Box Plot")

plt.boxplot(cars93["Price"])
plt.title("Box Plot")

plt.boxplot(cars93["Price"])
plt.title("Box Plot")

sns.boxplot(x="AirBags",y='Price',data=cars93)
plt.show()


#===============================================
g = sns.FacetGrid(cars93, col='AirBags')
g = g.map(plt.scatter,"EngineSize","MPG.highway")
plt.show()

#==============================================
g = sns.FacetGrid(cars93, row='AirBags')
g = g.map(plt.scatter,"EngineSize","MPG.highway")
plt.show()

plt.subplot(2,2,1)
sns.boxplot(y='Price',data=cars93)
plt.title("Box Plot")

plt.subplot(2,2,2)
sns.histplot(data=cars93,x='Price',bins=8)
plt.title("Histogram")

plt.subplot(2,2,3)
sns.scatterplot(data=cars93,x='Price', y='MPG.highway')
plt.title("Scaterplot")

plt.subplot(2,2,4)
a = cars93['AirBags'].value_counts()
a=a.plot(kind = 'bar')
plt.title("Barplot")
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()

a=cars93.groupby('AirBags')['Price'].mean()
a=a.plot(kind='bar')
plt.xticks(rotation=0)







