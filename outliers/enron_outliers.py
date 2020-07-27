#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL", 0)
data = featureFormat(data_dict, features)

for point in data:
    plt.scatter(point[0], point[1])
    if point[0]>1000000 and point[1]>5000000:
        print point[0], point[1]

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
### your code below
