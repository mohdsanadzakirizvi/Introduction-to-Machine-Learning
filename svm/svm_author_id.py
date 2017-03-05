#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC

clf = SVC(kernel='rbf', C=10000)

#Data set slicing to use only 1% of data
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t_train = time()
clf.fit(features_train,labels_train)
print 'Training time',round(time() - t_train, 3),'s'
t_pred = time()
pred = clf.predict(features_test)
print 'Predicting time',round(time() - t_pred, 3),'s'
#########################################################

from sklearn.metrics import accuracy_score

print "The accuracy of SVM is",round(accuracy_score(labels_test, pred),3)

print "10: %d,26: %d, 50: %d" %(pred[10],pred[26],pred[50])

c = 0
for p in pred:
	if p == 1:
		c += 1
print 'Count of Chris is',c
############ Plotting code ##############
# import matplotlib.pyplot as plt

# plt
