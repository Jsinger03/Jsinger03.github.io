#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi
import cgitb
import os
cgitb.enable()

def fs2d():
    #Convert return val of FieldStorage() into standard dictionary
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
    newpeople = open('user_pass.csv','a+')
    #users = ['dlup10,gamer\n', 'ninja,loser']
    for x in range(len(users)):
        users[x] = users[x].replace('\n','')
        users[x] = users[x].split(',')
    d = {}
    for x in users:
        d[x[0]] = x[1]
    #try:
    if ',' in input['password'] or ',' in input['username']:
        return "your password or username cannot have commas!!!"
    if input['username'] in d:
        return "username taken"
    else:
        newpeople.write(str('\n' + input['username'] + ',' + input['password']))
        newpeople.close()
        filename = 'userinfo/' + str(input['username']) + '.csv'
        x = open(filename,'w+')
        os.chmod(filename, 0o777)
        x.write(str(input['username']) + ',' + str(input['password']) + ',0,1,0,0,0')
        x.close()
        return 'signup succesful'
    #except:
        return "username or password not entered"

html_str="<html>"
html_str+="<head>"
html_str+="""<meta http-equiv="refresh" content="3; URL='./index.html'" /><link rel="stylesheet" type="text/css" href="../style.css" />
<link rel="icon" href="../famicon.png">
<title>Signup</title>"""
html_str+="</head>"
html_str+="<body><p>"
html_str+= str(helper())
html_str+="</p></body>"
html_str+="</html>"
print(html_str)
