#!/usr/bin/env python

import yfinance as yf
import sys

#para installar yfinance, rodar: pip install yfinance(nao eh necessario no replit)
#usagem: python nomedoscript.py TICKER, ou ./nomedoscript.py TICKER
#note que para rodar o script com ./ ao inves de python, deve-se ter a mesma coisa que tenho na linha numero 1 aqui(#!/usr/bin/env python)
#ticker = input('Type a stock :')
if len(sys.argv) < 2:
  print("ERROR: Must have at least 1 argument")
  sys.exit(1)

ticker = sys.argv[1]
stock = yf.Ticker(ticker)
stock_info = stock.info
market_price = stock_info['regularMarketPrice']
currency = stock_info['currency']
if market_price == "None":
  print("The provided ticker is either invalid and/or not available.")
  sys.exit(1)

print(f"{ticker.upper()} stock price: {market_price} {currency}")
print(f"Book value: {stock.info['bookValue']}")
print(f"Bid: {stock_info['bid']}")
print(f"Total Cash: {stock_info['totalCash']}")
print(f"Total Debt: {stock_info['totalDebt']}")
answer = input("Check financials? (yes/no): ")
if answer.lower() == "yes":
  print(stock.financials)
#use info keys para ver toda metadata que pode ser accessada.
#print(stock_info.keys())
#A fazer: permitir usar multiplos argumentos, e.g: stock.py MSFT, NFLX, NU(dica: for loop)