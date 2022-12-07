# MILESTONE PROJECT tests
import random #para a funcao random_play, jogada da IA
end_game = False
row1_list = [' ', ' ', ' ']
row2_list = [' ', ' ', ' ']
row3_list = [' ', ' ', ' ']
print('Welcome to the tic-tac-toe game player: X !')
print('Your enemy is the player: O !')
print('You have to mark your X signature three times to make a line diagonal, horizontal or vertical to win!')
print('Attention that your enemy will try to do the same!')

#function to print on the screen the game with the plays updated

def printer():
    print('Game:')
    print('\t COLUMNS')
    print('   1       2       3')
    print(f'1  {row1_list[0]:<5}|{row1_list[1]:^5}|{row1_list[2]:>5}')
    print('   _____|_____|_____')
    print(f'2  {row2_list[0]:<5}|{row2_list[1]:^5}|{row2_list[2]:>5}')
    print('   _____|_____|_____')
    print(f'3  {row3_list[0]:<5}|{row3_list[1]:^5}|{row3_list[2]:>5}')

# print error msgs
def repeat_msg():
    return print('Theres already an X or O inside this place!\nTry again!')

#user play input
def user_input():
    player = 'X'
    print(f'Your turn {player}!')
    while True:
        try:
            x_row = int(input('Choose a  row 1 to 3: '))
            x_column = int(input('Choose a column 1 to 3: '))
            if 1 <= x_row <= 3 and 1 <= x_column <= 3:
                print('Valid row and column number!\nChecking if the slot is empty...')
                break
            else:
                print('Only a row/column between 1 to 3 is valid!')
                continue
        except:
            print('Only a row/column between 1 to 3 is valid!')
    return x_row, x_column-1, player


#IA random play
def random_play():
    player = 'O'
    print('Enemy\'s turn!')
    random_row = random.randint(1,3)
    random_column = random.randint(1,3)
    print(f'Enemy row :{random_row}, Enemy column: {random_column}')
    return random_row, random_column-1, player

#function to verify empty spaces on the lists, if true mark user/IA desired play. 
# Problem! if IA runs 2 plays with the space is filled stop running the function random_play() to get more plays
def verify_space(row,column,player):
    global row1_list,row2_list,row3_list
    if player == 'X':
        if row == 1:
            if row1_list[column] != ' ':
                repeat_msg()
                user_input()
            else:
                row1_list[column] = 'X'
        elif row == 2:
            if row2_list[column] != ' ':
                repeat_msg()
                user_input()
            else:
                row2_list[column] = 'X'
        elif row == 3:
            if row3_list[column] != ' ':
                repeat_msg()
                user_input()
            else:
                row3_list[column] = 'X'
    else:
        if row == 1:
            if row1_list[column] != ' ':
                repeat_msg()
                random_play()
            else:
                row1_list[column] = 'O'
        elif row == 2:
            if row2_list[column] != ' ':
                repeat_msg()
                random_play()
            else:
                row2_list[column] = 'O'
        elif row == 3:
            if row3_list[column] != ' ':
                repeat_msg()
                random_play()
            else:
                row3_list[column] = 'O'  

#function to verify the winner, includes vertical horizontal and diagonal wins, or a draw is all spaces are filled
def verify_winner():
    global end_game
    global row1_list,row2_list,row3_list
    # X horizontal win --- for the 3 rows
    if row1_list == ['X']*3 or row2_list == ['X']*3 or row3_list == ['X']*3:  
        end_game = True
        print('You won the game! Horizontal win!')
    # O horizontal win --- for the 3 rows
    elif row1_list == ['O']*3 or row2_list == ['O']*3 or row3_list == ['O']*3: 
        end_game = True
        print('You lost the game! Enemy Horizontal win')
    # vertical win column 1
    elif row1_list[0] == row2_list[0] == row3_list[0] and row3_list[0] != ' ':
        if row3_list[0] == 'X':
            end_game = True
            print('You won the game! Vertical win!')
        else:
            print('You lost the game! Enemy Vertical win')
    #vertical win column 2
    elif row1_list[1] == row2_list[1] == row3_list[1] and row1_list[1] != ' ':
        if row1_list[1] == 'X':
            end_game = True
            print('You won the game! Vertical win!')
        else:
            print('You lost the game! Enemy Vertical win')
    # vertical win column 3
    elif row1_list[2] == row2_list[2] == row3_list[2] and row1_list[2] != ' ':
        if row1_list[2] == 'X':
            end_game = True
            print('You won the game! Vertical win!')
        else:
            print('You lost the game! Enemy Vertical win')
    #diagonal win \
    elif row1_list[0] == row2_list[1] == row3_list[2] and row1_list[0] != ' ':
        if row1_list[0] == 'X':
            end_game = True
            print('You won the game! Diagonal win!')
        else:
            print('You lost the game! Enemy Diagonal win')
    #diagonal win /
    elif row1_list[2] == row2_list[1] == row3_list[0] and row1_list[2] != ' ':
        if row1_list[0] == 'X':
            end_game = True
            print('You won the game! Diagonal win!')
        else:
            print('You lost the game! Enemy Diagonal win')
    #draw #DONT KNOW HOW TO DO AWAYS HIT THIS CONDITIONAL but with false
    #elif row1_list != ' ' or row1_list != 'X'*3 or row1_list != 'O'*3:
     #   if row2_list != ' ' or row2_list != 'X'*3 or row2_list != 'O'*3:
      #      if row3_list != ' ' or row3_list != 'X'*3 or row3_list != 'O'*3:  
       #         print('Its a draw! Try again!') 
    else:
        pass

while end_game == False:
    x = list(user_input())
    #print(x)
    verify_space(x[0],x[1],x[2])

    o = list(random_play())
    #print(o)
    verify_space(o[0],o[1],o[2])
    
    printer()
    verify_winner()