# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:37:57 2018

@author: JITESH
"""

x=raw_input()

import re

y=re.compile(r'^[+-]?[0-9]+\.[0-9]+$')

response=y.match(x)


if response:
    print True
else:
    print False