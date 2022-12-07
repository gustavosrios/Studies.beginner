#colecoes e listas
#create a shopping list and a price list for the items on the list
shop_list = ['rice','beans','meat','potatoes','carrot']
price_list = [15,10,25,10,10]
#loop that catches names and prices and print with $ before the price
for names, prices in zip(shop_list,price_list):
  print(names,'- $',prices)