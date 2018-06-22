# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:29:20 2018

@author: JITESH
"""

d=input()  



def fix_teen(y):
    if y>=13 and y<=19 and y is not 15 and 16:
        y=0
        return y
    else:
        return y

x=map(fix_teen,d.values())

print d
def sum(a,b):
    return a+b

print "Sum=",reduce(sum,x)

