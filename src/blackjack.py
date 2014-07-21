#!/usr/bin/python
'''
Created on Jul 19, 2014
@author: Satishkumar Masilamani
'''
import random

#This class initializes the Deck, here we are initializing single deck.
class Deck(object):
    #constructor
    def __init__(self):
        self.numbers=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.suits=["Spades","Clubs","Hearts","Diamonds"]
        self.cards=[]
        
    #method to create a single deck.
    def create_cards(self):
        for number in self.numbers:
            for suit in self.suits:
                self.cards = self.cards + [str(number) + ' ' + 'of' + ' ' + suit]
    
    #method to remove a randomly selected card from the deck. 
    def remove_card(self,card):    
        self.cards.remove(self.cards[card])

    #Every Time the user plays again, this method will recreate the single deck of cards.
    def recreate_deck(self):
        self.cards=[]
        self.create_cards()

#This class initializes the variable for each user and the actions associated with the user.
class Deal():
    #constructor
    def __init__(self,print_card_flag):
        self.user_cards=[]
        self.points=0
        self.totalpoints=0
        self.print_card_flag = print_card_flag              #determines either to print the card details
        self.user_type = print_card_flag                    #determines the type of user

    #Method which is used for the initial deal(2 cards for each user).
    def initial_deal(self):
        for i in range (1,3):
            random_pick_card = int(random.randrange(len(d.cards)-1))
            card = d.cards[random_pick_card]
            d.remove_card(random_pick_card)                 #call to remove the selected card from Deck
            self.user_cards.append(card)
            self.card_value_finder(card)                    #call to determine the value of the card
        self.print_card_details()                           #call to print the details of the card

    #Method which determines the value of the randomly selected card.
    def card_value_finder(self,card):
        #if the selected card is ACE then we have to decide the value of Ace has either 1 or 11
        if 'Ace' in card:
            one_eleven = 999
            one_eleven_rand = 999
            while(True):
                #if Ace is selected for User.
                if (self.user_type == 'Y'):
                    one_eleven = int(raw_input("Ace value has to be considered as 1 or 11..?"))
                #if Ace is selected for Dealer, select randomly.
                else:
                    one_eleven_rand=random.randrange(2)
                if one_eleven==1 or one_eleven_rand == 0:
                    self.points=1
                    print "Ace value considered as 1"
                    break
                elif one_eleven==11 or one_eleven_rand == 1:
                    self.points=11
                    print "Ace value considered as 11"
                    break
                else:
                    print "\nPlease enter a value either 1 or 11"
        elif ('10' in card or 'King' in card or 'Queen' in card or 'Jack' in card) :
            self.points=10            
        else:
            self.points = int(card[0:1])
        #once the value is determined add the value.
        self.totalpoints=self.totalpoints+self.points

    #Method to print the details of the card
    def print_card_details(self):
        for i in range(0,len(self.user_cards)):
            if (self.print_card_flag == 'Y' or ((self.print_card_flag == 'N') and (i == 0))):
                print "card " + str(i+1) + " : " + self.user_cards[i]
            else:
                print "card " + str(i) + " : *********************"
        if (self.print_card_flag == 'Y'):
            print "************************************* \nTotal Points : " + str(self.totalpoints)            

    #Method to perform the hit action of user/dealer.            
    def hit_action(self):
        random_pick_card = int(random.randrange(len(d.cards)-1))
        card = d.cards[random_pick_card]
        d.remove_card(random_pick_card)
        self.user_cards.append(card)
        self.card_value_finder(card)
        self.print_card_details()
        
#Method to provide the clear screen for each iteration.        
def cls():
    print "\n" * 100

#The Play starts from here    
def start_playing(betting_amount):
    #user object
    print "\n************************************* \nUser Cards : "
    user = Deal('Y')
    user.initial_deal()
    
    #dealer object
    print "\n************************************* \nDealer Cards : "
    computer = Deal('N')
    computer.initial_deal()
    print "\n*************************************"
    next_action = 1                                                             #initialize next action
    double_flag = 'N'                                                           #Flag for double down option
    
    #if the user gets 21 points in the initial Deal itself, then user wins.
    if user.totalpoints == 21:
        computer.print_card_flag = 'Y'
        print "\n************************************* \nDealer Cards : "
        computer.print_card_details()
        print "\n************************************* \nUser Cards : "
        user.print_card_details()
        print "\nwow.. That's a BlackJack...!"
        return betting_amount
    
    #if the user doesn't get a blackjack in the initial deal    
    while(True):
        print "\n*************************************"
        if (next_action == 1):
            next_action = int(raw_input("What do you want to do..? \n1. Hit\n2. Stand\n3. Double Down\n\n"))
        if (next_action == 1):                                                  #when user select Hit action
            print "\n************************************* \nUser Hits : User Cards..!"
            user.hit_action()
            print "\n************************************* \nDealer Cards : "
            computer.print_card_details()
            if (user.totalpoints > 21):
                print "\n************************************* \n"
                print "You are busted..."
                return (betting_amount * -1)
            else:
                continue
        elif (next_action == 2):                                                #when user selects stand or double down.
            print "\n*************************************"
            computer.print_card_flag = 'Y'
            if (computer.totalpoints < 17):
                print "\nDealer hits : Dealer Cards..!"
                computer.hit_action()
            elif(computer.totalpoints > 21):
                print "\n************************************* \nDealer Cards : "
                computer.print_card_details()
                print "\n************************************* \nUser Cards : "
                user.print_card_details()
                print "dealer is busted, you win"
                if (double_flag == 'Y'):
                    return (betting_amount * 1.5)
                else:
                    return betting_amount
            elif(computer.totalpoints > user.totalpoints):
                print "\n************************************* \nDealer Cards : "
                computer.print_card_details()
                print "\n************************************* \nUser Cards : "
                user.print_card_details()
                print "you lost"
                return (betting_amount * -1)
            elif(computer.totalpoints <= user.totalpoints):
                print "\n************************************* \nDealer Cards : "
                computer.print_card_details()
                print "\n************************************* \nUser Cards : "
                user.print_card_details()
                print "You win"
                if (double_flag == 'Y'):
                    return (betting_amount * 1.5)
                else:
                    return betting_amount                
        elif (next_action == 3):                                                    #when user selects double down action.
            print "\n************************************* \nUser Hits : User Cards..!"
            user.hit_action()
            double_flag = 'Y'
            next_action = 2
                        
        else:
            print "Please select either 1 or 2 as the option.."

#Get's the details of betting amount/chips, validates and then calls appropriate methods. 
def dealer_start(player_information):
    while(True):
        betting_amount = int(raw_input("You have " + str(player_information['Chips']) + " chips. \n\n" + "What is the bet you want to play for...? : "))
        if (betting_amount < 1):
            print "Betting Amount cannot be less than 1, Please bet at least 1."
            continue
        elif (betting_amount > player_information['Chips']):
            print "Betting Amount is more than the chips available, Please bet less than " + str(player_information['Chips'])
            continue
        else:
            player_information['Chips'] = player_information['Chips'] + start_playing(betting_amount)
            print ("You have " + str(player_information['Chips']) + " chips.")
            break

#Main : gets the information of the player.
def main():
    try:
        name = raw_input("Greeting...! Interested in playing BlackJack, Let's Play. \nWhat is your Name : ")
        player_information = {
        'FullName' : name,
        'Chips'    : 100
        }
        print "\n************************************* \n"
        print "Let's Play BlackJack " + player_information['FullName'] + " .."
        print "You are starting with : " + str(player_information['Chips']) + " Chips"
        while(player_information['Chips'] > 0):
            continue_playing = raw_input("\nDo you want to play a hand..? (y/n) ")
            d.recreate_deck()
            if (continue_playing == "y"):
                cls()
                dealer_start(player_information)
            elif (continue_playing == "n"):
                break
            else:
                print("The response was not valid, Please enter y or n")
                continue
        print "*******************Thank you for playing Blackjack, See you soon...!*******************"
    except Exception as e:
        raise e

#initialize the deck before the start of the game.
d=Deck()
d.create_cards()

if __name__ == '__main__':
    main()
    