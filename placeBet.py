#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi, cgitb, random
cgitb.enable()

inputs=cgi.FieldStorage()
user_info={}
for k in inputs.keys():
    user_info[k] = inputs[k].value

#---------------------setup stuff------------

def helper():
    input = user_info
    people = open('user_pass.csv','r+')
    users = people.readlines()
    people.close()
    htmlp0=""
    currentuser=[]
    for x in range(len(users)):
        users[x] = users[x].replace('\n','')
        users[x] = users[x].split(',')
    #users is now a list with sublists
    d = {}
    for x in users:
        d[x[0]] = x[1]
    #d is the passwords and usernames ONLY
    #try:
    #Opens the users file, containing nothing but the users info
    userfile = open('userinfo/' + str(input['username']) + '.csv','r+')
    currentuser = userfile.read().split(',')
            #removed  + random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 5])) so that the coin total is not modified
            #by going on this page
    z=[]
    y=user_info['username']
    z=[y]
    if '\r\n' in z[0]:
        z[0]=z[0].replace('\r\n','')
            #fixes the problem of \r\n being added in front of the username when returning from the game
        #below is the html page that allows the user to see their balance and place their bet for a game of blackjack
    htmlp0+='''<html>
    <head>
        <link rel="stylesheet" type="text/css" href="style.css" />
        <link rel="icon" href="blackjackicon.png">
        <title>Place Your Bet</title>
    </head>
    <body>
        <form class="lefto" name="ree" method="POST" action="login.py"><input type="hidden" name="username" value="''' + currentuser[0] + '''"><input type="hidden" name="password" value="''' + currentuser[1] + '''">
        <button>Go Back</button></form>
        <p>Welcome to the Blackjack table!
        <br>
        Your coin total is '''
    htmlp0+=str(int(currentuser[2]))
    htmlp0+='''
        </p>
        <form
        method="POST"
        action="game1.py"
        >
        <input type="number" name="bet" placeholder="Your Bet">
        <br>
        <input name="username" type="hidden"value="
'''
    htmlp0+=str(z[0])
    htmlp0+='''" style="visibility: hidden;"/>'''
    htmlp0 += '''<input name="password" type="hidden" value="'''
    htmlp0+=str(user_info['password'])
        #htmlp0+="<br>"
    htmlp0 += '''"style="visibility: hidden;"/><br><input type="submit" value="Deal" name="place bet">'''
    htmlp0+='''</form>'''
    htmlp0=str(htmlp0)
    if user_info['username'] in d:
        if user_info['password'] == d[user_info['username']]:
            return htmlp0
        else:
            return '''<meta http-equiv="refresh" content="3; URL='./index.html'" /></head><body><p>incorrect password</p>'''
    else:
        return '''<meta http-equiv="refresh" content="3; URL='./index.html'" /></head><body><p>usernonexistant</p>'''
    #except:
        #return '''<meta http-equiv="refresh" content="3; URL='./commiecoin.html'" /></head><body><p>username or password not entered</p>'''
htmlp0 = helper()
htmlp0+='''</body></html>'''
print(htmlp0)
