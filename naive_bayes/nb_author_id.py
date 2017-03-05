#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()
t_train = time()
clf.fit(features_train, labels_train)
print "time required to train",round(time()-t_train,3),'s'
t_predict = time()
# print features_train[0][0],'#'
pred = clf.predict(features_test)
print "time required to predict",round(time()-t_predict,3),'s'
# print pred
print accuracy_score(labels_tests,pred)

#########################################################


