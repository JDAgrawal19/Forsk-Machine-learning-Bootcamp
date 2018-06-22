# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:28:35 2018

@author: JITESH
"""

str1="""Forsk Technologies"""
print str1[-7:]
print str1[6]
print str1.upper()
print str1.lower()
print str1[-1]
print str1[::-1]

print str1.find('F')
print str1.replace('F','RA')

str2="Welcome to Marvel Cinematic universe"
print str2[::-1]
str2.split()

type(str2.split('m'))

'Marvel' in str2

" ".join(['hello','world'])


" Hy ".join(['hello','world'])

a='hello'
b='python'
print "%s %s" %(a,b)

str3=raw_input()

str3.replace(' ','*')

_2="Harry potter"

print _2

str4="A string is a sequence of zero or more characters"
str4.split(' ',5)

os="mac OS"
ver="6s"
mob="iphone"
print 'I have an {0} uses {2} and model {1}'.format(mob,ver,os)


str_1="Python Strings are, immutable sequence of characters"
str_1.find(',')