# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:44:44 2018

@author: JITESH
"""

x=raw_input()

y=list(x)
print y
#y.reverse()
def reverse(y):
    z=[]
    for i in y[::-1]:
        z.append(i)
    print "".join(z)
    
    

reverse(y)


