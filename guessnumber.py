# Write a program that when it starts generates a number between 1 and 10 and asks the user to guess a number. It's expected to say if the guess is higher or lower than the initial number or if he guessed right
import random

random_number = random.randint(1,10)
guess_right = False
guess = int(input('Type a number to guess:'))
if guess < 0:
  print('The number must be between 1 and 10!')
  guess = int(input('Type a number to guess:'))
if guess > 10:
  print('The number must be between 1 and 10!')
  guess = int(input('Type a number to guess:'))
while guess_right == False:
  if guess > random_number:
    print('Too high, try a lower number!')
    guess = int(input('Type a number to guess:'))
  if guess < random_number:
    print('Too low, try a higher number!')
    guess = int(input('Type a number to guess:'))
  if guess == random_number:
    print('Congratulations you have guessed right!')
    guess_right = True
    break