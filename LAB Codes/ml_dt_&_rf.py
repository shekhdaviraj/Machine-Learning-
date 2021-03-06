# -*- coding: utf-8 -*-
"""ML DT & RF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EHGehhiLlNzMqGoBNQvSBitMXFwZT5G_
"""

from google.colab import drive

drive.mount('/content/drive')

cd /content/drive/"MyDrive/ICT_ DEGREE/sem 6/ML"

ls

import numpy as np
import pandas as pd #panda used as csv file to convert into dataframe lib is used '''
import matplotlib.pyplot as plt #mathematical plotting library python 
features = pd.read_csv("temps.csv")

features

#mapping to number 
#considering a numerical value for the category
#one hot encoding 7 days

features.shape #rows * colm

features=pd.get_dummies(features) #creating dummy array

features

features.shape

labels=np.array(features['actual'])

#treat all value of one obsrv as different class for regression to classification problem

labels

features=features.drop('actual',axis=1)

features_list=list(features.columns)

features=np.array(features)

from sklearn.model_selection import train_test_split

train_features,test_features,train_labels,test_labels=train_test_split(features,labels,test_size=0.25)

train_features.shape

test_features.shape

from sklearn.ensemble import RandomForestRegressor

rf=RandomForestRegressor(n_estimators=1000)

rf

rf.fit(train_features,train_labels)

predictions=rf.predict(test_features)

predictions

test_labels #original values

errors=abs(predictions-test_labels)
#mean absolute error

mape=100*(errors/test_labels)

mean_error=np.mean(mape)

mean_error

accuaracy=100-mean_error

accuaracy

#visualize the trees: 1000 trees, 10th number tree

from sklearn.tree import export_graphviz
#.dot format -> model trained format of output 
#.dot format to png format for visualing tree
import pydot

tree=rf.estimators_[10]
export_graphviz(tree,out_file='RF_TREE.dot',feature_names=features_list)

(graph,)=pydot.graph_from_dot_file('RF_TREE.dot')
graph.write_png('RF tree.png')
#/content/drive/MyDrive/ICT_ DEGREE/sem 6/ML/RF_TREE.dot