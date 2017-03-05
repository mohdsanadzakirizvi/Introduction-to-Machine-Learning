#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from time import clock
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = DecisionTreeClassifier(min_samples_split=40)
time_t = clock()
clf = clf.fit(features_train,labels_train)
print 'Time taken to train',round(clock()-time_t,3),'s'
pred = clf.predict(features_test)
accuracy = accuracy_score(pred,labels_test)

print 'The accuracy is',round(accuracy,3)

print 'Number of features is',len(features_train[0]),

#########################################################


