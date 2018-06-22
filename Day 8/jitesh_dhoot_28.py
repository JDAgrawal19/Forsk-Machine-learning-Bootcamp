# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:16:48 2018

@author: JITESH
"""
list1=[]
list2=[]

def username(x="hjgg"):
    #print x
    for i in x:
        #print i
        if i.isdigit() or ord('A')<=ord(i)<=ord('Z') or ord('a')<=ord(i)<=ord('z') or i=='-' or i=='_':
            #print "digit n alphabates"
            continue
        else:
            #print"no alpha"
            return False
    return True

def website(x="hjkhkh"):
    for i in x:
        if i.isdigit() or ord('A')<=ord(i)<=ord('Z') or ord('a')<=ord(i)<=ord('z'):
            continue
        else:
            return False
    return True

def exten(x):
    if(len(x)<=3):
        return True
    else:
        return False
"""            
a=raw_input()
str3=(a.replace('@','.')).split('.')
print username(str3[0])
print website(str3[1])
print exten(str3[2])
"""

for i in range(0,int(input())):
    list1.append(raw_input())
    str1=(list1[i].replace('@','.')).split('.')
    if username(str1[0]) is True and website(str1[1]) is True and exten(str1[2]) is True :
        list2.append(list1[i])
    


list2.sort()