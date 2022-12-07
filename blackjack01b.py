import random
import time
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #tuple bc dont want change
ranks = ('2','3','4','5','6','7','8','9','10','J','Q','K','A') #tuple for every suit create rank
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
          '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
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
def start_msg():
    print('Welcome to the Blackjack CARD game!')
    time.sleep(1)
    print('Rules:')
    time.sleep(1)
    print('1-You and your opponent will get 2 cards,\nyou can win or lose the value of your bet')
    time.sleep(1)
    print('The cards value its the same of the number,\nexcept for J-Q-K that holds the same value: 10')
    time.sleep(1)
    print('Wins who gets closer to 21 win')
    time.sleep(1)
    print('Loses who gets above 21 on their sum, if both above 21,\nthe higher number loses.')
    time.sleep(1)
    print('2-If you and your opponent gets the same sum the round is a draw and\nwon\'t count')
    time.sleep(1)
    print('BONUS-The ACE card can be counted as 1 or 11, your choice!')
    time.sleep(1)
    print('The game starts in... \n  \t3')
    time.sleep(1)
    print('  \t2')
    time.sleep(1)
    print('  \t1')
    time.sleep(1)
    print('      START!')
def newcard_msg(name):
    print(f'{name} new cards:')
def hand_msg(name):
    print(f'{name} cards:')
def win_msg(name,bet):
    print(f'{name} Won ${bet},00!\n')
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self): #print cards to see what card is
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self):
        self.all_cards = [] #INTERNAL LIST OF CARD OBJECTS 
        for suit in suits: 
            for rank in ranks:
                new_card = Card(suit,rank) #class Card
                self.all_cards.append(new_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def hit_card(self):
        return self.all_cards.pop()
class Player:
    def __init__(self,name,bankroll): #input bankroll instanciando
        self.name = name
        self.bankroll = bankroll
    def bet(self):
        while True: # false
            amount = int(input('Your Bet:$'))
            try:
                if amount <= self.bankroll:
                    break
                else:
                    print('Invalid input, value must be lower or equal to your deposit.')
                    continue
            except:
                print('Invalid input, only numbers is allowed.')
                continue
        return amount
    def player_withdraw(self,amount):
        self.bankroll -= amount
    def player_deposit(self,amount):
        self.bankroll += amount
    def __str__(self): #print player mostrar $
        return f'{self.name} has ${self.bankroll},00'
class Dealer:
    def __init__(self,name):
        self.name = name
        self.bankroll = 1000000
    def dealer_withdraw(self,amount):
        self.bankroll -= amount
    def dealer_deposit(self,amount):
        self.bankroll += amount   
    def __str__(self):
        return f'{self.name} has ${self.bankroll},00'
def game():
    player_hand = []
    dealer_hand = []
    bet_amount = player.bet()
    add_cards = True
    total_dealer = 0
    total_player = 0
    #duas primeiras cartas coletar
    for i in range(0,2):
        player_hand.append(new_deck.hit_card())
        dealer_hand.append(new_deck.hit_card())
    hand_msg(player.name)
    for card in player_hand:
        printer(card)
    hand_msg(dealer.name)
    for card in dealer_hand:
        printer(card)
    #player turn
    while add_cards is True:
        try:
            add_another = input('Get another card? y/n\t')
        except:
            print('Invalid input. Type (y or n)')
            continue
        if add_another.lower() == 'y':
            player_hand.append(new_deck.hit_card())
            newcard_msg(player.name)
            for card in player_hand:
                printer(card)
                continue
        else:
            add_cards = False
            break
    for card in player_hand:
        if card.rank == 'A':
            a_value = int(input("Ace found. Do you want use 'A' as 11 or 1?: "))
            if a_value == 11:
                total_player += a_value      
            elif a_value == 1:
                total_player += a_value   
        else:
            total_player += card.value
    print(f'{player.name} Total value: {total_player}')
    #dealers turn
    for card in dealer_hand:
        total_dealer += card.value
    while True:
        if total_dealer <= total_player:
            dealer_hand.append(new_deck.hit_card())
            total_dealer += dealer_hand[-1].value
            continue
        else:
            break
    hand_msg(dealer.name)
    for card in dealer_hand:
        printer(card)
    print(f'{dealer.name} Total value: {total_dealer}\n')
     # compare sums
    if total_player > 21 and total_dealer <= 21: #dealer win - player busted
        win_msg(dealer.name,bet_amount)
        player.player_withdraw(bet_amount)
        dealer.dealer_deposit(bet_amount)
    elif total_dealer > 21 and total_player <= 21: #player win - dealer busted
        win_msg(player.name,bet_amount)
        dealer.dealer_withdraw(bet_amount)
        player.player_deposit(bet_amount)
    if total_dealer > 21 and total_player > 21:
        if total_player < total_dealer: #player win lesser number above 21
            win_msg(player.name,bet_amount)
            dealer.dealer_withdraw(bet_amount)
            player.player_deposit(bet_amount)
        else:                           #dealer win lesser number above 21
            win_msg(dealer.name,bet_amount)
            player.player_withdraw(bet_amount)
            dealer.dealer_deposit(bet_amount)
    if total_player <= 21 and total_dealer <= 21: #both below 21, whos higher wins
        if total_player > total_dealer:
            win_msg(player.name,bet_amount)
            dealer.dealer_withdraw(bet_amount)
            player.player_deposit(bet_amount)
        else:
            win_msg(dealer.name,bet_amount)
            player.player_withdraw(bet_amount)
            dealer.dealer_deposit(bet_amount)
    if total_player == total_dealer:
        print('Its a draw. Better luck next time!')
        pass
#instancing classes and game start
start_msg()
name = input('Name: ')
deposit = int(input(f'Hello, {name.title()}!\nDeposit a amount of money before begin:$'))
player = Player(name.title(), deposit)
dealer = Dealer('Dealer')
new_deck = Deck()
new_deck.shuffle()
game_on = True
while game_on is True:
    game()
    print(f'{player}')
    print(f'{dealer}')
    play_again = input('\n -> Want to play again?(y/n):  ')
    if play_again.lower() == 'y':
        continue
    else:
        print('Thanks for playing!')
        game_on = False
