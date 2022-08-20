# -*- coding: utf-8 -*-
"""Bitcoin_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CsQAcN7ozIl3HL9WZh9t1eRNrM-R4b9Y
"""

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

df = pd.read_csv("/content/bitcoin_price_bitcoin_price.2013Apr-2017Aug.csv")

df.describe()

df = df.drop(['Date'], axis = 1)
df

df = df.drop(df.index[1313:1557])

df = pd.DataFrame(df)

df['Volume'] = df['Volume'].str.replace(',', '').astype(int)

df['Market Cap'] = df['Market Cap'].str.replace(',', '').astype(int)

f,ax = plt.subplots(figsize=(12,8))
sns.heatmap(df.corr(), cmap="PuBu", annot=True, linewidths=0.5, fmt= '.2f',ax=ax)
plt.show()

df = preprocessing.scale(df)
df

df = pd.DataFrame(df)
df

X = df.drop([3], axis = 1)
X

# spliting the data into train and test sets

X = df.drop([3], axis = 1)
Y = df.iloc[:,3]

train_ratio = 0.70
test_ratio = 0.30

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 1-train_ratio, random_state = 1)

print(x_train, x_test, y_train, y_test)

Y

x_train

y_train

"""# **1) Decision Tree Regressor**"""

regressor = DecisionTreeRegressor()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
print(" The mean_squared_error for Decision Tree Regressor is -->",mean_squared_error(y_test, y_pred))

# varying hyper parameter

Max_depth =[2,3,4,5,8,9,10,11]
mse_hyper0 = []
for i in range(len(Max_depth)): 
   regressor = DecisionTreeRegressor(max_depth=Max_depth[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper0.append(mean_squared_error(y_test, y_pred))

print("mse_hyper0 :",mse_hyper0)
plt.xlabel("max_depth")
plt.ylabel("MSE")
plt.plot(Max_depth,mse_hyper0)
plt.show()

Min_samples_split=[2,3,4,5,6,7]
mse_hyper1 = []
for i in range(len(Min_samples_split)): 
   regressor = DecisionTreeRegressor(min_samples_split=Min_samples_split[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper1.append(mean_squared_error(y_test, y_pred))

print("mse_hyper1 :",mse_hyper1)
plt.xlabel("min_sample_split")
plt.ylabel("MSE")
plt.plot(Min_samples_split,mse_hyper1)
plt.show()




Min_samples_leaf=[1,2,3,4,5,6,7,9,10]
mse_hyper2 = []
for i in range(len(Min_samples_leaf)): 
   regressor = DecisionTreeRegressor(min_samples_leaf=Min_samples_leaf[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper2.append(mean_squared_error(y_test, y_pred))

print("mse_hyper2 :",mse_hyper2)
plt.xlabel("min_sample_leaf")
plt.ylabel("MSE")
plt.plot(Min_samples_leaf,mse_hyper2)
plt.show()


Min_weight_fraction_leaf=[0.1,0.2,0.3,0.4]
mse_hyper3 = []
for i in range(len(Min_weight_fraction_leaf)): 
   regressor = DecisionTreeRegressor(min_weight_fraction_leaf=Min_weight_fraction_leaf[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper3.append(mean_squared_error(y_test, y_pred))

print("mse_hyper3 :",mse_hyper3)
plt.xlabel("min_weight_fraction_leaf")
plt.ylabel("MSE")
plt.plot(Min_weight_fraction_leaf,mse_hyper3)
plt.show()


Max_features=[1,2,3,4,5]
mse_hyper4 = []
for i in range(len(Max_features)): 
   regressor = DecisionTreeRegressor(max_features=Max_features[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper4.append(mean_squared_error(y_test, y_pred))

print("mse_hyper4 :",mse_hyper4)
plt.xlabel("max_features")
plt.ylabel("MSE")
plt.plot(Max_features,mse_hyper4)
plt.show()

"""# **2). RandomForestRegressor**"""

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
print(" The mean_squared_error for Random Forest Regressor is -->",mean_squared_error(y_test, y_pred))

from sklearn.ensemble import RandomForestRegressor

# varying hyper parameter

Max_depth =[2,3,4,5,8,9,10,11]
mse_hyper0 = []
for i in range(len(Max_depth)): 
   regressor = RandomForestRegressor(max_depth = Max_depth[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper0.append(mean_squared_error(y_test, y_pred))

print("mse_hyper0 :",mse_hyper0)
plt.xlabel("max_depth")
plt.ylabel("MSE")
plt.plot(Max_depth,mse_hyper0)
plt.show()

N_estimator = [5,10,50,100,250]
mse_hyper1 = []
for i in range(len(N_estimator)): 
   regressor = RandomForestRegressor(n_estimators=N_estimator[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper1.append(mean_squared_error(y_test, y_pred))

print("mse_hyper1 :",mse_hyper1)
plt.xlabel("n_estimators")
plt.ylabel("MSE")
plt.plot(N_estimator,mse_hyper1)
plt.show()




Min_samples_leaf=[1,2,3,4,5,6,7,9,10]
mse_hyper2 = []
for i in range(len(Min_samples_leaf)): 
   regressor = RandomForestRegressor(min_samples_leaf=Min_samples_leaf[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper2.append(mean_squared_error(y_test, y_pred))

print("mse_hyper2 :",mse_hyper2)
plt.xlabel("min_sample_leaf")
plt.ylabel("MSE")
plt.plot(Min_samples_leaf,mse_hyper2)
plt.show()


Min_samples_split=[2,3,4,5,6,7]
mse_hyper1 = []
for i in range(len(Min_samples_split)): 
   regressor = RandomForestRegressor(min_samples_split=Min_samples_split[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper1.append(mean_squared_error(y_test, y_pred))

print("mse_hyper1 :",mse_hyper1)
plt.xlabel("min_sample_split")
plt.ylabel("MSE")
plt.plot(Min_samples_split,mse_hyper1)
plt.show()



Max_features=[1,2,3,4,5]
mse_hyper4 = []
for i in range(len(Max_features)): 
   regressor = RandomForestRegressor(max_features=Max_features[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper4.append(mean_squared_error(y_test, y_pred))

print("mse_hyper4 :",mse_hyper4)
plt.xlabel("max_features")
plt.ylabel("MSE")
plt.plot(Max_features,mse_hyper4)
plt.show()


Bootstrap =['True' , 'False']
mse_hyper4 = []
for i in range(2): 
   regressor = RandomForestRegressor(bootstrap=Bootstrap[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper4.append(mean_squared_error(y_test, y_pred))

print("mse_hyper4 :",mse_hyper4)
plt.xlabel("max_features")
plt.ylabel("MSE")
plt.plot(Bootstrap,mse_hyper4)
plt.show()

"""# **3. AdaBoostRegressor**"""

from sklearn.ensemble import AdaBoostRegressor
regressor = AdaBoostRegressor()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
print(" The mean_squared_error for Ada Boost Regressor is -->",mean_squared_error(y_test, y_pred))

from sklearn.ensemble import AdaBoostRegressor

# varying hyper parameter

N_estimator =[100,250,500,1000,2000]
mse_hyper1 = []
for i in range(len(N_estimator)): 
   regressor = AdaBoostRegressor(n_estimators=N_estimator[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper1.append(mean_squared_error(y_test, y_pred))

print("mse_hyper1 :",mse_hyper1)
plt.xlabel("n_estimators")
plt.ylabel("MSE")
plt.plot(N_estimator,mse_hyper1)
plt.show()




learning_rate=[0.001, 0.01, 0.1]
mse_hyper2 = []
for i in range(len(learning_rate)): 
   regressor = AdaBoostRegressor(learning_rate=learning_rate[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper2.append(mean_squared_error(y_test, y_pred))

print("mse_hyper2 :",mse_hyper2)
plt.xlabel("learning rate")
plt.ylabel("MSE")
plt.plot(learning_rate,mse_hyper2)
plt.show()

"""# **4) LinearRegression**"""

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
print(" The mean_squared_error for Linear Regressor is -->",mean_squared_error(y_test, y_pred))

"""# **5) KNeighborsRegressor**"""

from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
print(" The mean_squared_error for KNeighborsRegressor is -->",mean_squared_error(y_test, y_pred))

n_neighbors = [2, 5, 10, 15, 20, 25, 30]
mse_hyper1 = []
for i in range(len(n_neighbors)): 
   regressor = KNeighborsRegressor(n_neighbors=n_neighbors[i])
   regressor.fit(x_train, y_train)
   y_pred = regressor.predict(x_test)
   mse_hyper1.append(mean_squared_error(y_test, y_pred))

print("mse_hyper1 :",mse_hyper1)
plt.xlabel("n_neighbors")
plt.ylabel("MSE")
plt.plot(n_neighbors,mse_hyper1)
plt.show()

"""# **Hyper Tuning**"""

l =[]


regressor = DecisionTreeRegressor(max_depth = 10 , min_samples_leaf=2, min_samples_split=3, max_features = 3, min_weight_fraction_leaf =0.1 )
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
l.append(mean_squared_error(y_test, y_pred))


regressor = RandomForestRegressor(max_depth = 10 , n_estimators = 50, min_samples_leaf=1, min_samples_split=2, max_features = 5, bootstrap = True )
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
l.append(mean_squared_error(y_test, y_pred))

regressor = AdaBoostRegressor(n_estimators = 250 , learning_rate=0.1)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
l.append(mean_squared_error(y_test, y_pred))


regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
l.append(mean_squared_error(y_test, y_pred))

regressor = KNeighborsRegressor(n_neighbors = 2)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
l.append(mean_squared_error(y_test, y_pred))

l

model = ['DecisionTreeRegressor', 'RandomForestRegressor', 'AdaBoostRegressor', 'LinearRegressor', 'KNeighborsRegressor']

li = [model, l]
li

"""# **Table**"""

from tabulate import tabulate

print(tabulate({"Model": ['DecisionTreeRegressor',
  'RandomForestRegressor',
  'AdaBoostRegressor',
  'LinearRegressor',
  'KNeighborsRegressor'],"MSE": [0.10392068792329381,
  0.0017210892646876788,
  0.014899009499279232,
  0.0006486416067406132,
  0.003938337314564823]}, headers="keys", tablefmt="grid"))