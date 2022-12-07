'''
# Write a list that recieves the users 3 wishlist and print their availability, if available print the price
wish_01 = input('Type your wish list:')
wish_02


for wish in wish_list(input('Type your wish list:')):
print(wish[0],wish[1],wish[2])


list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[-1])
print(list_of_random_things[-2])
'''
'''
random_number_list = [25,26,27,28,29,30]
print(random_number_list[:4])  # so vai ate o 3 numero indexado no caso 28
print(random_number_list[1:]) 
print(random_number_list[4])   #printa 29 
'''
'''
list = ['Yesterday', 'Today', 'Tomorrow']
list[1] = 'I\'ve eaten a lot of potatoes, but i\'ll eat other stuff'
print(list)
list_02 = 'This is a string for checking the fifth index of the string'
print(list_02[5])

#lists exercises
#Quiz: List Indexing
#Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.
# Remember to account for zero-based indexing!
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month+1]

print(num_days)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[7:10])
print(eclipse_dates[-3:])
#print the first until up to the 3 lasts
print(eclipse_dates[:-3])
print(eclipse_dates[0:7])


#write a program that prints a str list using .join
new_list = "\n".join(['no','idea','to','put','elements','on','this','list'])
print(new_list)

new_list02 = "\nR$".join(['0','11','12','13'])
print(new_list02)

names = ["Kat", "gmail", "net"]
print(" @ ".join(sorted(names)))

#print the last element of a list
arr = [-10,1,4,55,100]
print(arr[len(arr) - 1])
'''
#TRAIN A LOT OF THIS STILL A LOT OF MISUNDERSTANDINGS.
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#print(arr[:3])  #prints the first three elements of the list
#print(arr[4:])  #PRINTS the last 3 elements of the list
print(*arr,sep=' ',)