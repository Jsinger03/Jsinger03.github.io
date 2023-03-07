#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi, random, cgitb
cgitb.enable()

cards=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
htmlp2=""

decision=cgi.FieldStorage()
testing={}
info={}

for k in decision.keys():
    testing[k] = decision[k].value
for k in testing.keys():
    info[k]=testing[k]
z=[]
y=info['username']
z=[y]
if '\r\n' in z[0]:
    z[0]=z[0].replace('\r\n','')
    #stops \r\n from getting added to the front of the username
#----------------setup for rest of game----------
def gamePlayer():
    player=int(info['player'])
    if info['action']=='hit':
        #if the player wishes to be dealt another card
        added=random.choice(cards)
        if added==11 and player>10:
            added-=10
            #if player gets dealt an ace and goes over 21, the ace acts as a 1
            #instead of an 11
        player += added
    return player
newHand=gamePlayer()

#------------------If the player hit, the above function gives them another card--------------------------------
dealer=info['dealer']
player=info['player']
htmlp2='''
<html>
        <head>
                <title>
                        Blackjack Simulator
                </title>
                <link rel="icon" href="../blackjackicon.png">
                <style>
                        body{
                        background-color: Green;
                        background-repeat: no-repeat;
                        background-position: center;
                        background-size: 1500px 803px}
                </style>
        </head>
        <body>
                <p style="text-align:center;"><font size="30" color="white">You may choose to hit or stay</font></p>'''
htmlp2+='''<p style="text-align:center;"><font size="15" color="white">your hand:'''
htmlp2+=str(newHand)
htmlp2+='</font></p>'
htmlp2+='''<p style="text-align:center;"><font size="15" color="white">dealer hand:'''
htmlp2+=str(dealer)
htmlp2+='</font></p>'
htmlp2+='''
                <form
                method="POST"
                action="game2.py"
                style="text-align:center;"
                >
                <input name="action" type="submit" value="hit" style="width: 10em;  height: 5em;"/>
                <br>
                <input checked="checked" name="player" type="radio" value="'''
htmlp2+=str(newHand)
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="dealer" type="radio" value="'''
htmlp2+=str(dealer)
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="username" type="radio"value="'''
htmlp2+=str(z[0])
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="password" type="radio"value="'''
htmlp2+=str(info['password'])
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="bet" type="radio"value="'''
htmlp2+=str(info['bet'])
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''</form>
                <form
                method="POST"
                action="game3.py"
                style="text-align:center;"
                >
                <input name="action" type="submit" value="stay" style="width: 10em;  height: 5em;"/>
                <br>
                <input checked="checked" name="player" type="radio" value="'''
htmlp2+=str(newHand)
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="dealer" type="radio" value="'''
htmlp2+=str(dealer)
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="username" type="radio"value="'''
htmlp2+=str(z[0])
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="password" type="radio"value="'''
htmlp2+=str(info['password'])
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''<input checked="checked" name="bet" type="radio"value="'''
htmlp2+=str(info['bet'])
htmlp2+='''" style="visibility: hidden;"/>'''
htmlp2+='''
                </form>
        </body>
</html>
'''

#--------------------HTML string to be output if the user does not bust-----------------------------

bet = int(info['bet'])
#sets a variable to the value of the user's bet
def losses():
    input=info
    people = open('user_pass.csv','r+')
    users = people.readlines()
    people.close()
    userfile = open('userinfo/' + str(input['username']) + '.csv','r+')
    currentuser = userfile.read().split(',')
    currentuser[2] = str(int(currentuser[2]) - bet)
            #subtracts the losses of the game of blackjack
    writtenoutput = ",".join(currentuser)
    fileo = open('userinfo/' + str(input['username']) + '.csv','w+')
    fileo.write(writtenoutput)
    fileo.close()
    return ""

#---------------function for updating the coin balance should the user bust--------

def bust():
    output=""
    if newHand > 21:
        #if the user busts, their coin balance gets updated with their loss
        losses()
        #if the user's hand goes above 21, then they bust and lose
        #this page gets output if this is the case
        output="""
<html>
        <head>
                <link rel="icon" href="blackjackicon.png">
                <title>
                        Blackjack Simulator Results
                </title>
                <style>
                        body{
                        background-color: Green;
                        background-repeat: no-repeat;
                        background-position: center;
                        background-size: 1500px 803px}
                </style>
        </head>
        <body>
            <p style="text-align:center;"><font size="30" color="white">HERE ARE THE RESULTS</font></p>
            <p style="text-align:center;"><font size="20" color="white"> You Bust :( """
        output+="<br>Your Hand:"
        output+=str(newHand)
        output+="""</font></p>
            <p style="text-align:center;"><font size="15" color="white">"""
            #<img src="https://media1.tenor.com/images/0603e2142ae26eac950f9dc9bad6db58/tenor.gif?itemid=13071756" allign="top">
        output += """<br>"""
        output += '''<form
                method="POST"
                action="placeBet.py"
                style="text-align:center;"
                >
                <input name="Play Again" type="submit" value="Play Another Round?" style="width: 15em;  height: 10em;"/>
                <br>
                <input checked="checked" name="player" type="radio"value="'''
        output+=str(player)
        output+='''" style="visibility: hidden;"/>'''
        output+='''<input checked="checked" name="dealer" type="radio" value="'''
        output+=str(dealer)
        output+='''" style="visibility: hidden;"/>'''
        output+='''<input checked="checked" name="username" type="radio"value="'''
        output+=str(z[0])
        output+='''" style="visibility: hidden;"/>'''
        output+='''<input checked="checked" name="password" type="radio"value="'''
        output+=str(info['password'])
        output+='''" style="visibility: hidden;"/>'''
        output+='''<input checked="checked" name="bet" type="radio"value="'''
        output+=str(info['bet'])
        output+='''" style="visibility: hidden;"/>'''
        output+='''
        </body>
    </html>
    '''
    else:
        #if the user has not bust, htmlp2 is output and the user may continue with the game
        output=htmlp2
    return output
print(bust())
