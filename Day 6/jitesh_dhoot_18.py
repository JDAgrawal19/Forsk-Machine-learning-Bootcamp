# -*- coding: utf-8 -*-
"""
Created on Sun May 20 15:35:40 2018

@author: JITESH
"""

x=raw_input()

def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            return False

    return True



if is_pangram(x) is True:
    print "PANGRAM"
else:
    print "NOT PANGRAM"