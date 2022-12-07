#If, Elif, Else
#In addition to the if clause, there are two other optional clauses often used with an if statement. For example:
'''season = str(input('What\'s the season?:'))
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

    Points	Prize
1 - 50	wooden rabbit
51 - 150	no prize
151 - 180	wafer-thin mint
181 - 200	penguin

points = 50  # use this input to make your submission
# write your if statement here
if points >= 1 and points <= 50:
    prize_name = 'wooden rabbit'
    result = "Congratulations! You won a",prize_name,"!"
elif points <= 150:
    result = 'Oh dear, no prize this time.'
elif points <= 180:
    prize_name = 'wafer-thin mint'
    result = "Congratulations! You won a",prize_name,"!"
elif points <= 200:
    prize_name = 'penguin'
    result = "Congratulations! You won a",prize_name,"!"
else: 
    print("Oh dear, no prize this time.")
print(result)


answer = int(input('Type your guess:'))
guess = int(input('Type your guess:'))

if int(answer) < int(guess):
    result = "Oops!  Your guess was too low."
elif int(answer) > int(guess):
    result = "Oops!  Your guess was too high."
elif int(answer) == int(guess):
    result = "Nice!  Your guess matched the answer!"

print(result)
#exercice 
state = 'CA'
purchase_amount = 100

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

weather = 'snow'
if weather == ("snow" or ""): # "" or '' means any other word than snow
  print('Wear boots!')
#good example
errors = 3
if errors: #clean code, nao preciso escrever errors == 3:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")
#In this code, errors has the truth value True because it's a non-zero number, so the error message is printed. This is a nice, succinct way of writing an if statement.
'''



points = 174 # use this as input for your submission

# establish the default prize value to None
prize = None
# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "water-thin mint"
elif points >= 181:
    prize = "penguin"
# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."
print(result)

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."
print(result)
