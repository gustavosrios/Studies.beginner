# Write your code here
def create_flowername(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            #COLETA ELEMENTO 0 DA LINHA, NO CASO A LETRA A NA PRIMEIRA ITERACAO e converte em letra minuscula
            value = line.split(': ')[0].lower()
            key = line.split(': ')[1].strip() # coleta elemento 1 da linha split pra tirar 2 pontos e espaco strip pular
            flower_dict[value] = key
    return flower_dict
# HINT: create a dictionary from flowers.txt
def input_name():
    dict_flower = create_flowername('flowers.txt')
    name = input('Name Surname (with space) : ')
    first_name = name[0]
    first_letter = first_name[0]
    print(f'Your flower name is: {dict_flower[first_letter]}')
input_name()
# HINT: create a function to ask for user's first and last name


# print the desired output

