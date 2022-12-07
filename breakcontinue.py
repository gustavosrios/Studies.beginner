'''
#write a program that recieves a shopping list and a storage list from the store, and counts if the item is on both of the lists.
wish_list = []
storage_list = ['screw', 'nail', 'cement', 'light bulb', 'electrical wires', 'electrical tape']
while wish_list != storage_list:
  wish = input('Type the product you want:')
  wish_list.append(wish)
  add_more = input('Add more products?: (Y/N)')
  if add_more == ('Y'):
    continue
  else:
    break
print('Searching our storage...')
for product in storage_list: 
  if product in wish_list:
    print('We have the product {}.'.format(product))
  if product not in wish_list:
    print('We have the product {} as well if you want to'.format(product))
print('This is your wish list:')
print(wish_list)

# correcting the condicionals
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]  #tuple of size 2
weight = 0
items = []
for cargo_name, cargo_weight in manifest: #para cada carga e seu peso dentro de manifest
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} / weight:{}".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} / weight:{}".format(cargo_name, cargo_weight))
        items.append(cargo_name) #coletando o nome da carga e adicionando na lista vazia names
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

#Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
#Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = "" #manchete
# write your loop here
for new in headlines:
  news_ticker += (new + ' ')
  if len(news_ticker) >= 140:
    news_ticker = news_ticker[:140]
    print(len(news_ticker))
    break
  else:
    continue
print(news_ticker)

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]
divisor = 1
for number in check_prime:
  if number % (divisor + 1) == 0 or number % (divisor + 2) == 0 or number % (divisor + 4) == 0:
    print('{} is not a prime number'.format(number))
  else:
    print('{} is a prime number'.format(number))
    continue
'''
 #UDACITY SOLUTION
check_prime = [26, 39, 51, 53, 57, 79, 85]
# iterate through the check_prime list
for num in check_prime:
# search for factors, iterating through numbers ranging from 2 to the number itself
  for i in range(2, num):
# number is not prime if modulo is 0
    if (num % i) == 0:
      print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
      break
# otherwise keep checking until we've searched all possible factors, and then declare it prime
    if i == num -1:    
      print("{} IS a prime number".format(num))