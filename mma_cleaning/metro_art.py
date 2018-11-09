import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#https://www.datacamp.com/community/tutorials/pandas-read-csv
#https://github.com/metmuseum/openaccess/
#Need to: specify what to do with missing values, specify dtypes and then read as csv

art = pd.read_csv('https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv')


art.head()
print('hi')
