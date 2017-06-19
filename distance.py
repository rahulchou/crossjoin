# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:07:51 2017

@author: rahul
"""

import pandas as pd

data = pd.read_csv('C:\\testdata.csv')
data2 = data.copy()
data2.columns = ['PIN2', 'LAT2', 'LONG2']
data_new = pd.DataFrame()

#first method, iterate over rows and concatenate rows
for i in range(len(data)):
    for j in range(len(data2)):
        #print('j is :'+ str(j))
        A = data.iloc[[i]].reset_index(drop=True)
        B = data2.iloc[[j]].reset_index(drop=True)
        temp = pd.concat([A,B],axis=1)
        data_new = data_new.append(temp)
data_new = data_new.reset_index(drop=True) 
#calculating distance 
data_new['DIS12'] = abs((data_new['LONG2']-data_new['LONG'])*(data_new['LAT2']-data_new['LAT']))

#alternate method using itertools library for cartesian product
import itertools
rows = itertools.product(data.iterrows(), data2.iterrows())
df = pd.DataFrame(left.append(right) for (_, left), (_, right) in rows)
df.reset_index(drop=True)
df['DIS12'] = abs((df['LONG2']-df['LONG'])*(df['LAT2']-df['LAT']))
