# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:30:07 2018

@author: JITESH
"""

x=raw_input()
y=[]
def translate(a):
    if(a==' '):
        y.append(' ')
    
    elif(a !='a' and a!='e' and a!='i' and a!='o' and a!='u'):
         y.append (a+'o'+a)
    else:
        y.append(a)
    
[translate(a) for a in x]

str1="".join(y)

print str1

