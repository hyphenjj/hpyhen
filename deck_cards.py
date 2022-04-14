#symbol = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
#make full deck
#then make random shuffle deck

import random
#start with our list of holders
cardfaces =[]
suits = ["♦", "♣", "♥", "♠"]
royals = ["J", "Q", "K","A"]
deck = []

#create a range using loops #this will add numbers starting from 2 -10 ending before 11
for i in range(2,11):
  cardfaces.append(str(i))

for j in range (4): #this will append the royals to the deck using the 4 royals J,Q,K,A
    cardfaces.append(royals[j])

for k in range(4):
    for l in range (13):
        card = (cardfaces[l] + " of " + suits[k]) #this will add the suit symbol to the card instead of the name can do both
        #makes each card, using suits through faces
        deck.append(card) #adds information to the deck

#shuffle deck uncomment below to get full deck comment out
#random.shuffle(deck)

#see the cards
for m in range(52):
    print(deck[m])

