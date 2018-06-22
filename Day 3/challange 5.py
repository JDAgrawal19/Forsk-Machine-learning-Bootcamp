# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:12:10 2018

@author: JITESH
"""


y=list(input()) 
y.sort()   

y.pop(len(y)-1)
y.pop(0)
count=0
for item in y:
    count+=item
count=count/len(y)
print count