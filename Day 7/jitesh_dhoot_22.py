    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import oauth2
import urllib2
import json
import time

url1 = "https://api.twitter.com/1.1/search/tweets.json" 

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }
    
consumer=oauth2.Consumer(key="	sHxIIacqOzagP0sOWvexVuIEF",
                         secret="MYJ28HJDIF8amIww93CSYPflHJiFgjE1emGLWWCDiBKcvmmj1C")

token=oauth2.Token(key="	159854868-umOhzzDEEODyhLgpxbq3iDjH0vLnPSsCyxJ1arcJ",
                   secret="aT7U4TNzFlrIn7Bd8bLZVkBZsYTa13kWcFWVTNiwLncLy")

params["oauth_consumer_key"] = consumer.key   # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key
params["q"] = "Jaipur"

req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))    


filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()