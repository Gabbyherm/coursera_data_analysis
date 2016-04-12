# -*- coding: utf-8 -*-
"""
Created on Saturday April 2 

@author: gabbyherm
"""

import pandas
import numpy

#import the entire dataset to memory
data = pandas.read_csv('addhealth_pds.csv', low_memory=False)

#upper-case all DataFrame column names - place afer code for loading data aboave
data.columns = map(str.upper, data.columns)

# bug fix for display formats to avoid run time errors - put after code for loading data above
pandas.set_option('display.float_format', lambda x:'%f'%x)

print('Number of observations: ', len(data))
print('Number of variables: ', len(data.columns))
print()

# ensure each of these columns are numeric
data['H1NB1'] = pandas.to_numeric(data['H1NB1'])
data['H1NB2'] = pandas.to_numeric(data['H1NB2'])
data['H1NB6'] = pandas.to_numeric(data['H1NB6'])

print('Counts for H1NB1 - know most people in neighborhood, yes=1')

# recode missing values to python missing (NaN)
data['H1NB1']=data['H1NB1'].replace(9, numpy.nan)
data['H1NB1']=data['H1NB1'].replace(8, numpy.nan)
data['H1NB1']=data['H1NB1'].replace(6, numpy.nan)

c1 = data['H1NB1'].value_counts(sort=False, dropna=False).sort_index()
print (c1)
print()

print('Percentage for H1NB1 know most people in neighborhood, yes=1')
p1 = data['H1NB1'].value_counts(sort=False, dropna=False, normalize=True).sort_index()
print (p1)
print()

# recode missing values to python missing (NaN)
data['H1NB2']=data['H1NB2'].replace(9, numpy.nan)
data['H1NB2']=data['H1NB2'].replace(8, numpy.nan)
data['H1NB2']=data['H1NB2'].replace(6, numpy.nan)

print('Counts for H1NB2 - talked with someone in neighborhood, yes=1')
c2 = data['H1NB2'].value_counts(sort=False, dropna=False).sort_index()
print (c2) 
print()

print('Percentage for H1NB2 talked with someone in neighborhood, yes=1')
p2 = data['H1NB2'].value_counts(sort=False, dropna=False, normalize=True).sort_index()
print (p2)
print()

print ('H1NB6 with Blanks set to NaN')
data['H1NB6']=data['H1NB6'].replace(9, numpy.nan)
data['H1NB6']=data['H1NB6'].replace(8, numpy.nan)
data['H1NB6']=data['H1NB6'].replace(6, numpy.nan)

print('Counts for H1NB6, happy living in neighborhood, 1=not at all, 5=very much')
c3 = data['H1NB6'].value_counts(sort=False, dropna=False).sort_index()
print (c3)
print()

print('Percentage for H1B6 happy living in neighborhood, 1=not at all, 5=very much')
p3 = data['H1NB6'].value_counts(sort=False, dropna=False, normalize=True).sort_index()
print (p3)

# Filtering out kids 17+ years old 

sub1 = data[(data['H1GI1Y']>=79)]

sub2=sub1.copy()

print('counts for 15 years old and younger according to year born')
c4=sub2['H1GI1Y'].value_counts(sort=False, dropna=False).sort_index()
print(c4)

#recoding values for H1GI1Y into a new variable, AGE_16Less, where year-born translated into age
recode1 = {79: 16, 80: 15, 81: 14, 82: 13, 83: 12}
sub2['AGELess16']= sub2['H1GI1Y'].map(recode1)

#Examining Frequency Distributions for Age
print ('Counts for AGELess16')
c5=sub2['AGELess16'].value_counts(sort=False, dropna=False).sort_index()
print(c5)

#print ('Percentage of AGEless16')
#p5=sub2('AGELess16').value_counts(sourt=False, dropna=False, normalize=True).sort_index()
#print(p5)