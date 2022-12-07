
import yfinance as yf

forex_data = yf.download('BRLUSD=X', start='2021-01-02', end='2022-12-31')
print(forex_data)

#!/usr/bin/env python

#importar api do yahoo e o modulo basico time para fazer pause no tempo
import yfinance as yf
import time

#pegando o nome da ação
resposta = input("Digite o nome da ação: ")

#invocamos o modulo Ticker do yafinance(importado como yf) para adquirir os dados da ação
stock = yf.Ticker(resposta)
#dados armazenados na variavel stock_info
stock_info = stock.info

print("Agora vou te mostrar toda a metadata que voce pode usar\n")

#3 segundos de pausa
time.sleep(3)

#o abaixo printa todas as metadatas presentes usando o metodo "keys", que são meramente chaves de um dicionário
print(stock_info.keys())
#o \n printa uma linha nova(linha em branco)
print("---------------\n")

print(
  "Agora vamos testar algumas destas metadata pra ver oque podemos vizualizar")

#loop infinito
while True:
  metadata = input(
    "Digite o nome da metadata(para cancelar digite FIM). exemplo: regularMarketPrice: "
  )
  #se digitar FIM, o loop é quebrado. Como não tem mais código depois disso, o programa é fechado.
  if metadata == "FIM":
    break

  #chamamos a metadata com stock.info['nomedametadata'], como estamos usando uma variavel que armazena uma string, nao precisamos usar aspas, fornecendo somente o nome da variavel.
  data = stock.info[metadata]
  print(f"{metadata}: {data}")