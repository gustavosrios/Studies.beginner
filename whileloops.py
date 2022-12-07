'''
#write a program that recieves users account balance in bank and his bills, and retrieves the sum of the bills from the bank acc.
bank_money = int(input('Your account balance:'))
bills = {}
bill_name = input('Bill name:')
bill_price = int(input('Bill price:'))
bills[bill_name] = bill_price

while sum(bills.get(bill_name)) < 1000:
  bank_money -= bill_price
print(bank_money)

#Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.
#Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?
#After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the case that break_num should be a number that is the first number larger than end_num.

start_num =  #provide some start number
end_num = 10 #provide some end number that you stop when you hit
count_by = 1 #provide some number to count by 
break_num = start_num
# write a condition to check that end_num is larger than start_num before looping
if start_num >  end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
  result = break_num
  while break_num < end_num: # 10 < 10: falso
    break_num += count_by # 3 = 3 + count(1)
    result = break_num
print(result)


#Quiz: Nearest Square
#Write a while loop that finds the largest square number less than an integer limit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
#For example, if limit is 40, your code should set the nearest_square to 36.
# write your while loop here 
#TENHO QUE PEGAR UM NUMERO ELEVAR AO QUADRADO E VERIFICAR SE E MENOR QUE 40
num = 0
limit = 40
while (num+1)**2 < limit:
  num = num + 1
  total = num**2
  
print(total)
'''
# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers. 
#Would you use a while or a for loop to write this code?
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
counter = 0
for num in num_list:
  if (num % 2) != 0:
    num_list.append(num)
    counter += 1  
  if counter == 5:
    print(num_list)
    break
#use the same code to give a sum of the all odd numbers
