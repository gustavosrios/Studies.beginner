
#Print vs. Return in Functions
#Here are two valid functions. One returns a value and one simply prints a value, without returning anything. Test run this code and experiment to understand the difference.
# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(20) #ATRIBUINDO ESSA VARIAVEL A FUNCAO NO CASO AGORA SERIA SO PRA PRINTAR NA TELA E TBM ATRIBUINDO O VALOR AO PARAMETRO NUM 20
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(120) # CALLING FUNCTON: STORING VALUE ON THE OBJECT, 120 = NUM
print('Done calling')
print('This function returned: {}'.format(return_value_2))