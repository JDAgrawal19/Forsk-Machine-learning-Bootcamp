# -*- coding: utf-8 -*-
"""
Created on Thu May 24 22:26:21 2018

@author: JITESH
"""

import requests

url_s= "http://13.127.155.43/api_v0.1/sending"
url_r= "http://13.127.155.43/api_v0.1/receiving?Phone_Number=9413600451"

data={
      "Phone_Number" :"9413600451",
       "Name" : "jitesh",
       "College_Name" : "jecrc",
        "Branch" :"ece"
      }

send_data=requests.post(url_s,json=data)

print send_data.text

receive_data=requests.get((url_r))

print receive_data.text

