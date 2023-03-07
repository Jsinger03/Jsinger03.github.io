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
    #try:
    if input['username'] in d:
          if input['password'] == d[input['username']]:
              return success(d, input, users)
          else:
              return '''<meta http-equiv="refresh" content="2; URL='./index.html'" /></head><body><p>wrong password</p>'''
    else:
        return '''<meta http-equiv="refresh" content="2; URL='./index.html'" /></head><body><p>usernonexistant</p>'''
    #except:
        #return '''<meta http-equiv="refresh" content="2; URL='./index.html'" /></head><body><p>username or password not entered</p>'''

def success(dic, input, userinfo):
    output = '''</head><body><button onclick="window.location.href = './index.html';">Log Out</button>'''
    #<----------->
    #Opens the users file, containing nothing but the users info
    userfile = open('userinfo/' + str(input['username']) + '.csv','r+')
    currentuser = userfile.read().split(',')
    #<----------->
    try:
        if input['upgrade'] == "2x multiplier: 100CC":
            if int(currentuser[2]) >= 100:
                currentuser[2] = str(int(currentuser[2])-100)
                currentuser[3] = "2"
        if input['upgrade'] == "3x multiplier: 500CC":
            if int(currentuser[2]) >= 500:
                currentuser[2] = str(int(currentuser[2])-500)
                currentuser[3] = "3"
        if input['upgrade'] == "4x multiplier: 1000CC":
            if int(currentuser[2]) >= 1000:
                currentuser[2] = str(int(currentuser[2])-1000)
                currentuser[3] = "4"
        if input['upgrade'] == "5x multiplier: 2000CC":
            if int(currentuser[2]) >= 2000:
                currentuser[2] = str(int(currentuser[2])-2000)
                currentuser[3] = "5"
        if input['upgrade'] == "Win The Game: 10000CC":
            if int(currentuser[2]) >= 10000:
                currentuser[2] = str(0)
                currentuser[3] = str(1)
                currentuser[4] = str(int(currentuser[4]) + 1)
        if input['upgrade'] == "Mark of Stalin: 10 Wins":
            if int(currentuser[4]) >= 10:
                currentuser[2] = str(0)
                currentuser[3] = str(1)
                currentuser[4] = str(0)
                currentuser[5] = str(1)
    except:
        currentuser[2] = str(int(currentuser[2]) + (int(currentuser[3]) * (int(currentuser[4]) + 1)))
    output += "<p>Welcome " + input['username'] + " <br>Your current balance is " + currentuser[2] + "<br> Your multiplier is " + str(int(currentuser[3]) * (int(currentuser[4]) + 1)) + "x"
    if currentuser[4] != '0':
        if currentuser[4] == "1":
            output += '''</p><p>Comrade, the true winner is he who gives his money to Mother Russia!<br>You have won the game ''' + currentuser[4] + " time"
        else:
            output += '''</p><p>Comrade, the true winner is he who gives his money to Mother Russia!<br>You have won the game ''' + currentuser[4] + " times"
    if currentuser[5] != '0':
        if currentuser[5] == "1":
            output += '''</p><p>Stalin has given you his mark ''' + currentuser[5] + " time"
        else:
            output += '''</p><p>Stalin has given you his mark ''' + currentuser[5] + " times"
    output += '''</p><div class="stuff"><form name="ree" method="POST" action="login.py"><input type="hidden" name="username" value="''' + currentuser[0] + '''">'''
    output += '''<input type="hidden" name="password" value="''' + currentuser[1] + '''">
    <button>Work The Farms</button></div></form>
    '''
    output += '''<form method="POST" action="placeBet.py">
                <input name="game" type="submit" value="play blackjack"/><br>
                <input name="coins" type="hidden" value="''' + str(currentuser[2]) + '''">'''
    output += '''<input name="username" type="hidden" value="''' + str(input['username']) + '''">'''
    output += '''<input name="password" type="hidden" value="''' + str(input['password']) + '''">'''
    output += '''</form>'''
    #numerouno = olduserinfo[0]
    #for x in range(len(olduserinfo)):
    #    if int(olduserinfo[x][2]) >= int(numerouno[2]):
    #        numerouno = olduserinfo[x]
    output += '''<form name="input" method="POST" action="login.py"><input type="hidden" name="username" value="''' + currentuser[0] + '''">'''
    output += '''<input type="hidden" name="password" value="''' + currentuser[1] + '''"><select name="upgrade" size="1" >'''
    if currentuser[3] == '1':
        output += '''<option checked="checked">2x multiplier: 100CC</option>'''
    elif currentuser[3] == '2':
        output += '''<option checked="checked">3x multiplier: 500CC</option>'''
    elif currentuser[3] == '3':
        output += '''<option checked="checked">4x multiplier: 1000CC</option>'''
    elif currentuser[3] == '4':
        output += '''<option checked="checked">5x multiplier: 2000CC</option>'''
    else:
        output += '''<option checked="checked">Win The Game: 10000CC</option>'''
    if currentuser[4] != "0":
        output += '''<option checked="checked">Mark of Stalin: 10 Wins</option>'''
    output +='''
    </select>
    <button>BUY!</button>
    </form>'''
    #if currentuser[0] == numerouno[0]:
    #    output += '<p> Congrats comrade! You are best communist!</p>'
    #else:
    #    output += '<p>The best communist is "' + numerouno[0] + '" with ' + numerouno[2] + ' Commie Coins</p>'
    #<--------->
    #WRITES THE FILE FOR THE USER ONLY
    writtenoutput = ",".join(currentuser)
    fileo = open('userinfo/' + str(input['username']) + '.csv','w+')
    fileo.write(writtenoutput)
    fileo.close()
    #<---------->
    return output

html_str="<html>"
html_str+="<head>"
html_str+="""<link rel="stylesheet" type="text/css" href="style2.css" />
<link rel="icon" href="../famicon.png">
<title>Commie Coin</title>"""
html_str+= str(helper())
html_str+="</body>"
html_str+="</html>"
print(html_str)
