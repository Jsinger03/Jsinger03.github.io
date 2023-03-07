#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import random, cgi, math
cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
playercard1=random.choice(cards)
playercard2=random.choice(cards)
#generates the rwo cards that will make up the user's hand
player = playercard1 + playercard2
#player=21
dealercard1= random.choice(cards)
dealer = dealercard1
suits=["&hearts;","&clubs", "&spades;", "&diams;"]
#generates a random hand for the player and shows one card for the dealer, as per
#the rules of blackjack

if player==22:
    player-=10
    #the ace can be 11 or 1 depending on if it makes the user bust if it is 11

info={}
inputs=cgi.FieldStorage()
for k in inputs.keys():
    info[k] = inputs[k].value
#info={'username': '\r\njsinger10', 'bet': '5', 'place bet': 'Deal', 'password': '1234'}
z=[]
y=str(info['username'])
z=[y]
#print(z)
if '\r\n' in z[0]:
    z[0]=z[0].replace('\r\n','')
    info['username']=str(z[0])
    #gets rid of \r\n appearing at front of username
#print(z, info)

#-----------------------------------Setup of game above--------------
currentBalance=0
def invalidBet():
    input=info
    people = open('user_pass.csv','r+')
    users = people.readlines()
    people.close()
    currentuser=[]
    if 'bet' in info.keys():
        #if a bet was placed, this will check if it is valid
        #try:
            userfile = open('userinfo/' + str(input['username']) + '.csv','r+')
            currentuser = userfile.read().split(',')
            #print(currentuser)
            if abs(int(info['bet'])) > int(currentuser[2]):
                #if the bet is larger than the user's coin balance, they get returned to the index page
                return'''<meta http-equiv="refresh" content="3; URL='index.html'" /></head><body><p>invalid bet</p>'''
            else:
                #sets the current balance to the user's coin total
                currentBalance = currentuser[2]
                info['bet']= str(abs(int(info['bet'])))
                return currentBalance
        #except:
            #print("get nae naed")
            #if no bet was placed, then a placeholder bet is inserted and they are returned to the index
            info['bet']=''
            return'''<meta http-equiv="refresh" content="3; URL='index.html'" /></head><body><p>invalid bet</p>'''
    else:
        info['bet']=0
        return'''<meta http-equiv="refresh" content="3; URL='index.html'" /></head><body><p>invalid bet</p>'''

invalidBet()
#----------------------Checks the bet to make sure it is valid above--------------
htmlp1="""
<html>
        <head>
                <link rel="icon" href="blackjackicon.png">
                <title>
                        Blackjack Simulator
                </title>"""
htmlp1+="""
                <style>
                        body{
                        background: Green;
                        color: #CC0033;
                        background-repeat: no-repeat;
                        background-position: center;
                        background-size: 1500px 803px
}
                </style>
        </head>
        <body>"""
            #<h1 style="text-align:center;">
            #<img src="https://media3.giphy.com/media/l2Sq2mPVJr4tfk436/source.gif" align="top"></h1>"""
htmlp1+='''<br><p style="text-align:center;"><font size="15" color="white">your hand:'''
htmlp1+=str(player)
htmlp1+='''</font></p>'''
#https://htmyell.com/creating-playing-cards-with-css-html/
# used the link above to learn how to create playing cards
htmlp1+='''<p style="text-align:center;"><font size="15" color="white"> dealer hand:'''
htmlp1+=str(dealer)
htmlp1+='''</font></p>'''
htmlp1+='''<p style="text-align:center;"><font size="15" color="white"> Your bet:'''
htmlp1+=str(info['bet'])
htmlp1+='</font></p>'
htmlp1+='''
                <form
                method="POST"
                action="game2.py"
                style="text-align:center;"
                >
                <input name="action" type="submit" value="hit" style="width: 10em;  height: 5em;"/>
                <br>
                <input checked="checked" name="player" type="radio"value="'''
htmlp1+=str(player)
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="dealer" type="radio" value="'''
htmlp1+=str(dealer)
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="username" type="radio"value="'''
htmlp1+=str(z[0])
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="password" type="radio"value="'''
htmlp1+=str(info['password'])
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="bet" type="radio"value="'''
htmlp1+=str(info['bet'])
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''
                </form>
                <form
                method="POST"
                action="game3.py"
                style="text-align:center;"
                >
                <input name="action" type="submit" value="stay" style="width: 10em;  height: 5em;"/>
                <br>
                <input checked="checked" name="player" type="radio"value="'''
htmlp1+=str(player)
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="dealer" type="radio" value="'''
htmlp1+=str(dealer)
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="username" type="radio"value="'''
htmlp1+=str(z[0])
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="password" type="radio"value="'''
htmlp1+=str(info['password'])
htmlp1+='''" style="visibility: hidden;"/>'''
htmlp1+='''<input checked="checked" name="bet" type="radio"value="'''
htmlp1+=str(info['bet'])
htmlp1+='''" style="visibility: hidden;"/><br>'''

#-----------The html string above is the output so long as the user does not get blackjack and places a valid bet----------

try:
    #
    currentBalance=int(invalidBet())
except:
    currentBalance=0
#-----create the variable of the user's current balance
try:
    bet=int(info['bet'])
except:
    bet=""
#------creates a variable for the user's bet
try:
    if bet*2 < currentBalance:
    #allows the user to double his bet and gain one more card, as per the rules of blackjack
        htmlp1+='''<input name="action" type="submit" value="double down" style="width: 10em;  height: 5em;"/>
            <br>
            <input checked="checked" name="player" type="radio"value="'''
        htmlp1+=str(player)
        htmlp1+='''" style="visibility: hidden;"/>'''
        htmlp1+='''<input checked="checked" name="dealer" type="radio" value="'''
        htmlp1+=str(dealer)
        htmlp1+='''" style="visibility: hidden;"/>'''
        htmlp1+='''<input checked="checked" name="username" type="radio"value="'''
        htmlp1+=str(z[0])
        htmlp1+='''" style="visibility: hidden;"/>'''
        htmlp1+='''<input checked="checked" name="password" type="radio"value="'''
        htmlp1+=str(info['password'])
        htmlp1+='''" style="visibility: hidden;"/>'''
        htmlp1+='''<input checked="checked" name="bet" type="radio"value="'''
        htmlp1+=str(info['bet'])
        htmlp1+='''" style="visibility: hidden;"/>'''
        htmlp1+='''
                </form>
        </body>
</html>
'''
except:
    #if the user cannot double down, then the closing of the html string is added to htmlp1
    htmlp1+='''
                </form>
        </body>
</html>
'''
#----------Allows the user to double down above-----------------

def winnings():
    input=info
    people = open('user_pass.csv','r+')
    users = people.readlines()
    people.close()
    userfile = open('userinfo/' + str(input['username']) + '.csv','r+')
    currentuser = userfile.read().split(',')
    currentuser[2] = str(int(currentuser[2]) + (bet * 2))
    #subtracts the losses of the game of blackjack
    writtenoutput = ",".join(currentuser)
    fileo = open('userinfo/' + str(input['username']) + '.csv','w+')
    fileo.write(writtenoutput)
    fileo.close()
    return ""

#-------------function for updating the user's coin balance if they get blackjack---------

def blackjack():
    output=""
    continueGame=str(invalidBet())
    if continueGame!='''<meta http-equiv="refresh" content="3; URL='index.html'" /></head><body><p>invalid bet</p>''':
        #if the bet placed was valid
        if player==21:
            #if the player has blackjack, a different html page is generated and their coin balance gets updated with 2x what they bet
            winnings()
            output="""
<html>
        <head>
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
            <p style="text-align:center;"><font size="20" color="white"> YOU GOT BLACKJACK!!!</font><br>
            <img src="https://media2.giphy.com/media/l0HlvGBz8LSYQlA5y/giphy.gif" align="bottom"></br>
            </p>"""
            output += '''<form
                method="POST"
                action="placeBet.py"
                style="text-align:center;"
                >
                <input name="Play Again" type="submit" value="Play Another Round?" style="width: 15em;  height: 10em;"/>
                <br>'''
            output+='''<input checked="checked" name="username" type="radio"value="'''
            output+=str(z[0])
            output+='''" style="visibility: hidden;"/>'''
            output+='''<input checked="checked" name="password" type="radio"value="'''
            output+=str(info['password'])
            output+='''" style="visibility: hidden;"/>'''
            output+='''
                </form>
        </body>
</html>
'''
        #creates a special page for if the user gets blackjack
        #this page will update the coin total and present a button to return
        #to the placeBet.py page and place another bet
        elif player<21 and continueGame!='''<meta http-equiv="refresh" content="3; URL='index.html'" /></head><body><p>invalid bet</p>''':
            output=htmlp1
            #if the bet is valid and the user does not get blackjack, takes htmlp1 and sets that as they page to be genrated
    if continueGame=='''<meta http-equiv="refresh" content="3; URL='index.html'" /></head><body><p>invalid bet</p>''':
        #if the bet placed was invalid, the following is output to let the user know about their invalid bet
        output="""
<html>
        <head>
                <title>
                        Blackjack Simulator Results
                </title>"""
        output +='''<meta http-equiv="refresh" content="3; URL='index.html'" /></head><body><p>invalid bet</p>'''
        output += """
                <style>
                        body{
                        background-color: Green;
                        background-repeat: no-repeat;
                        background-position: center;
                        background-size: 1500px 803px}
                </style>
        </head>"""
    return output
print(blackjack())

            
