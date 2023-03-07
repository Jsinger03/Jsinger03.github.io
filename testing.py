#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi
import cgitb
import random

cgitb.enable()

def fs2d():
    d = {}
    L = []
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def helper():
    input = fs2d()
    people = open('user_pass.csv','r+')
    users = people.readlines()
    people.close()
    for x in range(len(users)):
        users[x] = users[x].replace('\n','')
        users[x] = users[x].split(',')
    #users is now a list with sublists
    d = {}
    for x in users:
        d[x[0]] = x[1]
    #d is the passwords and usernames ONLY
    try:
        if input['username'] in d:
              if input['password'] == d[input['username']]:
                  return input
              else:
                  return '''<meta http-equiv="refresh" content="2; URL='./index.html'" /></head><body><p>wrong password</p>'''
        else:
            return '''<meta http-equiv="refresh" content="2; URL='./index.html'" /></head><body><p>usernonexistant</p>'''
    except:
        return '''<meta http-equiv="refresh" content="2; URL='./index.html'" /></head><body><p>username or password not entered</p>'''

html_str="<html>"
html_str+="<head>"
html_str+="""<link rel="stylesheet" type="text/css" href="../style.css" />
<link rel="icon" href="../famicon.png">
<title>Commie Coin</title>"""
html_str+= str(helper())
html_str+="</body>"
html_str+="</html>"
print(html_str)
