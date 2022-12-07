# Write a program that recieves the users data, stocks list and price he paid for the stock when he bought it
print("Hello! This program will help you see your stocks and price much easier!")
name = input("Name: ")
print("Hello,",name,"Now we will need what stocks you bought and the price you\'ve paid for them'!")
stocks_end = False
stocks_list = []
stock_prices = []
while stocks_end == False:
  stocks = input('Stock:')
  stocks_list.append(stocks)
  print('Now the price you\'ve paid!')
  price = input('Price:')
  stock_prices.append(price)
  add_more = str(input('Want to add more? Yes or No:'))
  if add_more == ('yes' or 'Yes'):
    stocks = input('Stock:')
    stocks_list.append(stocks)
    print('Now the price you\'ve paid!')
    price = input('Price:')
    stock_prices.append(price)
    add_more = str(input('Want to add more? Yes or No:'))
  if add_more == ('no' or 'No'):
    stocks_end = True
for stocks, price in zip(stocks_list,stock_prices):
  print('Stock:',stocks,'- $',price)