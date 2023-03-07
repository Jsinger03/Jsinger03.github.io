#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi, random
cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
info={}
decision=cgi.FieldStorage()
for k in decision.keys():
    info[k] = decision[k].value
z=[]
y=info['username']
z=[y]
if '\r\n' in z[0]:
    z[0]=z[0].replace('\r\n','')
    #stops the username from getting messed up
#------------------setup for finishing the game---------------

def gameDealer():
    dealer=int(info['dealer'])
    dealer+=random.choice(cards)
    #adds the dealer's second card (previously hidden from view)
    if dealer >= 17:
        #the dealer CANNOT hit once the value of the hand is greater than or
        #equal to 17
        return dealer
    while dealer < 17:
        #so long as the dealer's hand is less than 17, they must hit
        dealer+= random.choice(cards)
    return dealer

#-----------------simulates the dealer's hand according to the rules of blackjack--------

def doubleDown():
    player=int(info['player'])
    if info['action']=='double down':
        #if the player wishes to be dealt another card
        added=random.choice(cards)
        if added==11 and player>10:
            added-=10
            #if player gets dealt an ace and goes over 21, the ace acts as a 1
            #instead of an 11
        player += added
    return int(player)
#---------------function for simulating user's hand if they doubled down--------------

#function for updating coin balance if the user wins
def winnings():
    input=info
    people = open('user_pass.csv','r+')
    users = people.readlines()
    people.close()
    userfile = open('userinfo/' + str(input['username']) + '.csv','r+')
    currentuser = userfile.read().split(',')
    currentuser[2] = str(int(currentuser[2]) + int(info['bet']))
            #subtracts the losses of the game of blackjack
    writtenoutput = ",".join(currentuser)
    fileo = open('userinfo/' + str(input['username']) + '.csv','w+')
    fileo.write(writtenoutput)
    fileo.close()
    return ""

#---------------function for updating user's coin balance if they win----------

#adjusts the coin balance if the user loses
def losses():
    input=info
    people = open('user_pass.csv','r+')
    users = people.readlines()
    people.close()
    userfile = open('userinfo/' + str(input['username']) + '.csv','r+')
    currentuser = userfile.read().split(',')
    currentuser[2] = str(int(currentuser[2]) - int(info['bet']))
            #subtracts the losses of the game of blackjack
    writtenoutput = ",".join(currentuser)
    fileo = open('userinfo/' + str(input['username']) + '.csv','w+')
    fileo.write(writtenoutput)
    fileo.close()
    return ""

#------------function for updating user's coin balance if they lose----------

def results():
    player=int(info['player'])
    dealer=gameDealer()
    result=""
    gif=""
    output=[player, dealer]
    if info['action']=='double down':
        #if the player has doubled down, they get dealt another card and their bet gets doubled
        #the rest of the game is simulated from there
        playerhand=doubleDown()
        #playerhand is the players new hand value after doubling down
        info['bet']=str(int(info['bet']) * 2)
        #doubles the bet
        output[0]=playerhand
        if playerhand > 21:
            result="You Bust"
            gif='''<img src="https://i.gifer.com/94x3.gif" align="top">'''
            output.append(result)
            output.append(gif)
            losses()
            return output
        elif dealer > 21:
            result="Dealer Busts! You Win"
            gif='''<img src="https://media1.tenor.com/images/5917355c058854d9ff724079482240ec/tenor.gif?itemid=10410009" align="top">'''
            output.append(result)
            output.append(gif)
            winnings()
            return output
        elif playerhand > dealer:
            result="You Win"
            gif='''<video width="320" height="240" autoplay>
            <source src="https://giant.gfycat.com/DentalCompassionateHerald.webm" type="video/mp4">
            No video for you
            </video>'''
            output.append(result)
            output.append(gif)
            winnings()
            return output
        elif playerhand < dealer:
            result="You Lose"
            gif='''<img src="https://thumbs.gfycat.com/BouncyIllegalBlowfish-max-1mb.gif" align="top">'''
            output.append(result)
            output.append(gif)
            losses()
            return output
        elif playerhand==dealer:
            result="Push!"
            gif='''<img src="https://thumbs.gfycat.com/GregariousOddballAnemoneshrimp-size_restricted.gif" align="top">'''
            output.append(result)
            output.append(gif)
            return output
    #determines the results of the match and creates the appropriate message
    #if the user has not doubled down, the game is simulated given the relevant inputs from the previous pages and the results are generated
    elif player > 21:
        result="You Bust"
        gif='''<img src="https://i.gifer.com/94x3.gif" align="top">'''
        output.append(result)
        output.append(gif)
        losses()
        return output
    elif dealer > 21:
        result="Dealer Busts! You Win"
        gif='''<img src="https://media1.tenor.com/images/5917355c058854d9ff724079482240ec/tenor.gif?itemid=10410009" align="top">'''
        output.append(result)
        output.append(gif)
        winnings()
        return output
    elif player > dealer:
        result="You Win"
        gif='''<video width="320" height="240" autoplay>
            <source src="https://giant.gfycat.com/DentalCompassionateHerald.webm" type="video/mp4">
            No video for you
            </video>'''
        output.append(result)
        output.append(gif)
        winnings()
        return output
    elif player < dealer:
        result="You Lose"
        gif='''<img src="https://thumbs.gfycat.com/BouncyIllegalBlowfish-max-1mb.gif" align="top">'''
        output.append(result)
        output.append(gif)
        losses()
        return output
    elif player==dealer:
        result="Push!"
        gif='''<img src="https://thumbs.gfycat.com/GregariousOddballAnemoneshrimp-size_restricted.gif" align="top">'''
        output.append(result)
        output.append(gif)
        return output

#-------------function for determining the results of the game of blackjack---------------

final=results()
htmlp3="""
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
            <p style="text-align:center;"><font size="30" color="white">HERE ARE THE RESULTS</h1><h3 style="text-align:center;">"""
htmlp3+=str(final[2])
htmlp3+="""<br>"""
#htmlp3+=str(final[3])
#stopped gifs because they are unnecessary
htmlp3+=""" </p><br>
            <p style="text-align:center;"><font size="15" color="white">"""
htmlp3+="your hand:"
htmlp3+=str(final[0])
htmlp3+='<br>'
htmlp3+="dealer's hand:"
htmlp3+=str(final[1])
htmlp3+="<br>"
htmlp3+="Your bet:"
htmlp3+=str(info['bet'])
htmlp3+="</p>"
htmlp3+='''<form
                method="POST"
                action="placeBet.py"
                style="text-align:center;"
                >
                <input name="Play Again" type="submit" value="Play Another Round?" style="width: 15em;  height: 10em;"/>
                <br>
                <input checked="checked" name="player" type="radio"value="'''
htmlp3+=str(final[0])
htmlp3+='''" style="visibility: hidden;"/>'''
htmlp3+='''<input checked="checked" name="dealer" type="radio" value="'''
htmlp3+=str(final[1])
htmlp3+='''" style="visibility: hidden;"/>'''
htmlp3+='''<input checked="checked" name="username" type="radio"value="'''
htmlp3+=str(info['username'])
htmlp3+='''" style="visibility: hidden;"/>'''
htmlp3+='''<input checked="checked" name="password" type="radio"value="'''
htmlp3+=str(info['password'])
htmlp3+='''" style="visibility: hidden;"/>'''
htmlp3+='''<input checked="checked" name="bet" type="radio"value="'''
htmlp3+=str(info['bet'])
htmlp3+='''" style="visibility: hidden;"/>'''
htmlp3+='''</form>
        </body>
    </html>
    '''
#-------------------the HTML string that gets output at the end with the results, and a button allowing the user to place another bet and play again
print(htmlp3)
