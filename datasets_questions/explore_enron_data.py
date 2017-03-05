#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
names_list = open("../final_project/poi_names.txt","r")

count_poi,count_poi_nan=0,0
for person in enron_data:
	if enron_data[person]["total_payments"] == 'NaN' and enron_data[person]["poi"] == True:
		count_poi_nan += 1
	if enron_data[person]["poi"] == True:
		count_poi += 1
print count_poi_nan,(count_poi_nan/(count_poi_nan+count_poi+0.0))*100

print count_poi