
number = int(input('Type a number to calculate its fatorial:'))
fatorial = 1
if number < 0:
  print('The number must be positive(above zero)')
  number = int(input('Type a number to calculate its fatorial:'))
if number > 0:
  for item in range(1,number +1):
    fatorial = fatorial * item
    print(fatorial)


#understand better this - for item in range function
#FATORIAL WITH WHILE LOOP
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while number != 1:
  number -= 1
  current += 1
  product *= current
# udacity answer
while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1
print(product)
# multiply the product so far by the current number

# increment current with each iteration until it reaches number

# print the factorial of number

#Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num.
#  Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

#Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? 
# What condition will you use to see when it's time to stop looping?

#After the loop is done, print out break_num, showing the value that indicated it was time to stop looping.
#  It is the case that break_num should be a number that is the first number larger than end_num.

# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# write your for loop here
for item in range(1,number+1):
  product = product * item
  #product += (number * item)

# print the factorial of number
print(product)
