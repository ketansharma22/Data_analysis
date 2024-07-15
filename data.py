import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #visualizing data
import seaborn as sns

#import csv file
df=pd.read_csv('Data.csv',encoding='unicode_escape')

#drop blank/unused columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)

# droping null values
df.dropna(inplace=True)

# renaming of columns(optional)
df.rename(columns={'Marital_Status':'Shadi'},inplace=True)
print(df.info())

#Exploratory Data analysis
