#!/usr/bin/python

# Allow inline plotting of figures.
#%matplotlib inline

# Import useful libraries.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

# Read in the file URL.
fileURL = './NewClusterSheet.csv'


# Read the file into a DataFrame.
data = pd.read_csv(fileURL)

#Replace nominal data with integers
data = data.replace(['H','M','R',''],[1,1,1,0])

#replace with median
cols = data.dtypes
for key, value in cols.items():
    if key != "Class":
        data[key].fillna(data[key].median(),inplace=True)

print data