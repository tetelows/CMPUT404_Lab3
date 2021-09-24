#!/usr/bin/env python3

import os, json

print("Content-type:text/html\r\n\r\n")
print
print("<title> Test CGI</title>")
print("<p> Hellow World Cmput 404 class!</p>")

#Q1
print("os.environ")
json_object = json.dumps(dict(os.environ), indent=4)
print(json_object)

#q2
for param in os.environ.keys() :
    if (param=="QUERY STRING") :
        #print (f"<em>(param}</em>={os.environ[param]]</li>")
        print ("<b>%20s</b>: %s<br>" % (param, os. environ[param]))
#03

for param in os. environ.keys () :
    if (param=="HTTP USER AGENT") :
        print ("<b>%20s</b>: %s<br>" % (param, os.environ[param]))