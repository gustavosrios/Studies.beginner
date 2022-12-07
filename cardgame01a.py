import random
import time
game_end = False
card_p1 = [] #Player1 hand list of cards
card_p2 = [] #Player2 hand list of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #tuple bc dont want change
ranks = ('2','3','4','5','6','7','8','9','10','J','Q','K','A') #tuple  for every suit create rank
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
          '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def printer(card):
    if card.suit == 'Spades':
        suit = '♠'
        print(f'|{card.rank:<7}|')
        print(f'|{suit:^7}|')
        print(f'|{card.rank:>7}|')
    if card.suit == 'Hearts':
        suit = '♥'
        print(f'|{card.rank:<7}|')
        print(f'|{suit:^7}|')
        print(f'|{card.rank:>7}|')
    if card.suit == 'Diamonds':
        suit = '♦'
        print(f'|{card.rank:<7}|')
        print(f'|{suit:^7}|')
        print(f'|{card.rank:>7}|')
    if card.suit == 'Clubs':
        suit = '♧'
        print(f'|{card.rank:<7}|')
        print(f'|{suit:^7}|')
        print(f'|{card.rank:>7}|')
def msg_start():
    print('Welcome to the card WAR game.')
    print('The rules are simple, you and your adversary will be given 2 decks with 26 cards.')
    print('You get one card from the deck, and the DUEL begins!')
    print('Who gets the higher card wins and gets the adversary\'s card. Loses who don\'t have any cards!')
    print('But in case of a draw we will have the WAR time!')
    print('On WAR you will bet 3 more cards and will DUEL again for the draw + bet to get all the cards!')
    print('The game starts in... \n  \t3')
    time.sleep(1)
    print('  \t2')
    time.sleep(1)
    print('  \t1')
    time.sleep(1)
    print('      START!')
def duel_msg():
    print('\nDUEL TIME!\n')
    time.sleep(3)
def duel_winner(player):
    print(f'\n{player} has won the duel!\n')
    time.sleep(2)
def war_msg():
    print('\nDRAW! WAR TIME!\n')
    time.sleep(4)
def war_duel():
    print('\nWAR DUEL!')
def war_winner(player):
    print(f'\n{player} has won the WAR!\n')
    time.sleep(2)
def duel_printer(card_01,card_02):
    print('Gustavo\'s CARD')
    printer(card_01)
    print('\n:::VERSUS:::\n')
    print('Opponent\'s CARD')
    printer(card_02)
def win_msg(player_name):
    print(f'\nNo cards left!\n{player_name} has won the game!')
def clear_cards(card_01,card_02):
    card_p1.clear()
    card_p2.clear() 
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self): #print cards to see what card is
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self):
        self.all_cards = [] #INTERNAL LIST OF CARD OBJECTS / atributo pra receber lista de TODAS as cartas
        '''
        LOOP FOR EACH SUIT GET ALL THE RANKS
        suit[0] HEARTS > rank[0] 2,3,4,5,6,7,8,9,j,q,k,a
        suit[1] Diamonds > rank[0] 2,3,4,5,6,7,8,9,j,q,k,a 
        '''
        for suit in suits: 
            for rank in ranks:
                new_card = Card(suit,rank) #class Card
                self.all_cards.append(new_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_card(self):
        self.all_cards.pop() 
class Player:
    '''
    Classe sera usada para obter a atual lista de cartas, 
    player should be able to add or remove cards from their ''hand''  (the list of card objects)
    player needs to add one or multiple cards to their list of cards
    '''
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def shuffle(self):
        random.shuffle(self.all_cards)
    def remove_one(self):
        if self.all_cards != []:
            return self.all_cards.pop(0)
        else:
            pass
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards) #if its list add with extend
        else:
            self.all_cards.append(new_cards) # if its individual card add with append  
    def __str__(self): #print how many cards player has in hand
        return f'{self.name} has {len(self.all_cards)} cards.'
def duel(): #usar clear() no final
    global card_p1,card_p2,game_end
    while True:
        if len(player_01.all_cards) == 0:
            win_msg(player_02.name)
            game_end = True
            break
        if len(player_02.all_cards) == 0:
            win_msg(player_01.name)
            game_end = True
            break
        duel_msg()
        card_p1.append(player_01.remove_one())
        card_p2.append(player_02.remove_one())
        duel_printer(card_p1[-1],card_p2[-1])
        if card_p1[-1].value == card_p2[-1].value:
                war_msg()
                war()
                continue
        if card_p1[-1].value > card_p2[-1].value:
            player_01.add_cards(card_p1[-1])
            player_01.add_cards(card_p2[-1])
            clear_cards(card_p1,card_p2)
            duel_winner(player_01.name)
            print(player_01)
            print(player_02)
            player_01.shuffle()
            continue
        if card_p1[-1].value < card_p2[-1].value:
            player_02.add_cards(card_p1[-1])
            player_02.add_cards(card_p2[-1]) 
            clear_cards(card_p1,card_p2)
            duel_winner(player_02.name)
            print(player_01)
            print(player_02)
            player_02.shuffle()  
            continue
        #if len(player_01.all_cards) + len(player_02.all_cards) == 52:
         #   continue
        #else:
        #    break
def war():
    global card_p1,card_p2,game_end
    war_duel()
    while True:
        for num in range(0,7):
            if len(player_01.all_cards) != 0:
                card_p1.append(player_01.remove_one())
            if len(player_02.all_cards) != 0:
                card_p2.append(player_02.remove_one())
        duel_printer(card_p1[-1],card_p2[-1])
        if card_p1[-1].value == card_p2[-1].value:
            continue
        elif card_p1[-1].value > card_p2[-1].value:
            player_01.add_cards(card_p1)
            player_01.add_cards(card_p2)
            war_winner(player_01.name)
            print(player_01)
            print(player_02)
            player_01.shuffle()
            break
        elif card_p1[-1].value < card_p2[-1].value:
            player_02.add_cards(card_p1)
            player_02.add_cards(card_p2)
            war_winner(player_02.name)
            print(player_01)
            print(player_02)
            player_02.shuffle()
            break
    duel() 
#instancing classes and game start 
msg_start()           
player_01 = Player('Gustavo')
player_02 = Player('Opponent')
new_deck = Deck()
new_deck.shuffle()
counter = 0
for card in new_deck.all_cards:
    counter += 1
    if counter <= 26:
        player_01.add_cards(card)     
    if counter > 26:
        player_02.add_cards(card)
while game_end is False: 
    duel()