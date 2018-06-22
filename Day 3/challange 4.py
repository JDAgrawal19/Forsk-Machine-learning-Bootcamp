# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:23:07 2018

@author: JITESH
"""

str1=raw_input()
x=0
y=0

for item in str1:
    if  item.isdigit():
        x+=1;
    elif item.isalpha():
        y+=1;

print "Letters ",y
print "Digits ",x
        