# repeat loops and lists
'''
# write a message on the screen 4 times 
for palavra in range(1,4):
    print('carregando')
    
'''

'''
# range(1,20) vai de 1 a 19
for item in range(1,20):
    print('billy')
'''

'''
# range (2,12,2) vai de 2 a 10 de dois em dois, 2-4-6-8-10
for item in range(2,12,2):
  print(item)
  '''


'''
  #write a program that write the users name and age the same amount of times as the age of the user. (random ideas)
  
nome_pessoa = input('Your name:')
idade = input('Your age?')
for item in range(1,int(idade)):
  print(idade)
for item in range(1,int(idade)):
  print(nome_pessoa)
'''

'''
#write a names list
names = ['Joao','Jose','Maria','Conceicao']
for names in names:
  print(names)
# escreva um programa que recebe uma lista de nomes e printa eles na tela
names = input('Escreva os nomes seguido de espaco')
for item in names:
  print(names)
'''

# Print values from 1 to N (n being the variable input by the user)
user_value = int(input('Insert a number: '))
start_value = 1
user_value = user_value + 1
for start_value in range(start_value,user_value):
  print(start_value)