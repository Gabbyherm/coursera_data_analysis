# -*- coding: utf-8 -*-
"""
Created on Saturday April 2 

@author: gabbyherm
"""

import pandas
import numpy


data = pandas.read_csv('addhealth_pds.csv', low_memory=False)

#upper-case all DataFrame column names - place afer code for loading data aboave
data.columns = map(str.upper, data.columns)

# bug fix for display formats to avoid run time errors - put after code for loading data above
pandas.set_option('display.float_format', lambda x:'%f'%x)

print('Number of observations: ', len(data))
print('Number of variables: ', len(data.columns))
print()

data['H1NB1'] = pandas.to_numeric(data['H1NB1'])
data['H1NB2'] = pandas.to_numeric(data['H1NB2'])
data['H1NB6'] = pandas.to_numeric(data['H1NB6'])

print('Counts for H1NB1 - know most people in neighborhood, yes=1')

c1 = data['H1NB1'].value_counts(sort=False).sort_index()
print (c1)
print()

print('Percentage for H1NB1 know most people in neighborhood, yes=1')
p1 = data['H1NB1'].value_counts(sort=False, normalize=True).sort_index()
print (p1)
print()

print('Counts for H1NB2 - talked with someone in neighborhood, yes=1')
c2 = data['H1NB2'].value_counts(sort=False).sort_index()
print (c2) 
print()

print('Percentage for H1NB2 talked with someone in neighborhood, yes=1')
p2 = data['H1NB2'].value_counts(sort=False, normalize=True).sort_index()
print (p2)
print()

print('Counts for H1NB6, happy living in neighborhood, 1=not at all, 5=very much')
c3 = data['H1NB6'].value_counts(sort=False).sort_index()
print (c3)
print()

print('Percentage for H1B6 happy living in neighborhood, 1=not at all, 5=very much')
p3 = data['H1NB6'].value_counts(sort=False, normalize=True).sort_index()
print (p3)
