import random
import re


class Deck:

  

    def __init__(self):
        Deck.d1=[]
        Deck.v1=[None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "king"]
        Deck.c1=["Clubs", "Diamonds", "Hearts", "Spades"]
        #Adding all the cards to the list d1 which will be our deck
        for i in range(1, 14):
            for j in range(0, 4):
                Deck.d1.append(Deck.v1[i]+" of "+Deck.c1[j])


class Cards:
    #creating a random number, which we use as an index in d1 to get back whatever is at that index like "4 of hearts" for example
    def __init__(self):
        Cards.card1=Deck.d1[random.randint(0, 51)]
        Cards.card2=Deck.d1[random.randint(0, 51)]
        
        Deck.d1.remove(Cards.card1)
        Deck.d1.remove(Cards.card2)
        
            
            

    def compare_cards():
        #Here we use a regular expression to find all occurences of any value a card can have, like "2" or "king"
        #The findall method then returns a list with all the occurences that matched what was described
        Deck()
        Cards()
        card1_value=re.findall("Ace|2|3|4|5|6|7|8|9|10|Jack|Queen|king", Cards.card1)
        card2_value=re.findall("Ace|2|3|4|5|6|7|8|9|10|Jack|Queen|king", Cards.card2)
        

        #Now we put in that list as an element and try and get the index that that element represent in the value list, first we put in 0 to the list...
        #that findall method gave us, this should. this list will only contain one element but we want it as a string so therefore we put in the 0...
        #the list might be card1_value=["Ace"] so card1_value="Ace", then we use that as to find its index
        
        card1_value=Deck.v1.index(card1_value[0])
        card2_value=Deck.v1.index(card2_value[0])
        
        

        if card1_value>card2_value:
            Win.player_winning1()
            string1="{}'s {} won over {}'s {}"
            string1=string1.format(PlayGame.player1, Cards.card1, PlayGame.player2, Cards.card2)
            print()
            print(string1)
        if card1_value<card2_value:
            Win.player_winning2()
            string1=("{}'s {} won over {}'s {}")
            string1=string1.format(PlayGame.player2, Cards.card2, PlayGame.player1, Cards.card1)
            print()
            print(string1)
        if card1_value==card2_value:
            Cards.compare_color()
            if Cards.color1>Cards.color2:
                Win.player_winning1()
                string1="{}'s {} won over {}'s {} with color"
                string1=string1.format(PlayGame.player1, Cards.card1, PlayGame.player2, Cards.card2)
                print()
                print(string1)

            if Cards.color1<Cards.color2:
                Win.player_winning2()
                string1="{}'s {} won over {}'s {} with color"
                string1=string1.format(PlayGame.player2, Cards.card2, PlayGame.player1, Cards.card1)
                print()
                print(string1)
                

    def compare_color():
        Cards.color1=re.findall("Clubs|Diamonds|Hearts|Spades",Cards.card1)
        Cards.color2=re.findall("Clubs|Diamonds|Hearts|Spades",Cards.card2)
        Cards.color1=Deck.c1.index(Cards.color1[0])
        Cards.color2=Deck.c1.index(Cards.color2[0])

class Win:
    
    def __init__(self):
        Win.player1=0
        Win.player2=0
    def player_winning1():
        Win.player1+=1
    def player_winning2():
        Win.player2+=1
        
      
            
    
        
class PlayGame:
    def play_game():
        Win()
        print("""This is WAR, both of you will draw one card, the person with highest value will win, when a player has won seven times the game will stop and they declared the victor!""")
        a=input("press any key to start! ")
        PlayGame.player1=input("Player 1 type your name! ")
        PlayGame.player2=input("Player 2 type your name! ")
        if not a==None:
            while Win.player1<7 and Win.player2<7:
                Cards.compare_cards()
                a=input("press c to do the next round, press any other letter to quit! ")
                if a=="c":
                    pass
                if not a=="c":
                    break
        if Win.player1>Win.player2:
            print()
            print(PlayGame.player1+" has won the game of WAR!, thanks for playing:)")
        if Win.player1<Win.player2:
            print()
            print(PlayGame.player2+" has won the game of WAR!, thanks for playing:)")
                
            
            
    
   
PlayGame.play_game()

