# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:54:28 2016

@author: gabbyherm
"""


data = pandas.read_csv('addhealth_pds.csv', low_memory=False)

#upper-case all DataFrame column names - place afer code for loading data aboave
data.columns = map(str.upper, data.columns)

# bug fix for display formats to avoid run time errors - put after code for loading data above
pandas.set_option('display.float_format', lambda x:'%f'%x)

print('Number of observations: ', len(data))
print('Number of variables: ', len(data.columns))
print()

data['AgeEst']=data[1994-'H1GI1Y']

