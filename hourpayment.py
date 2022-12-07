#exercicio 01 - Write a program that calculates the value paid per hour with the monthly payment and hours worked on that month
salario_mensal = input('What is your monthly payment')
horas_trabalhadas = input('How many hours have you worked this month?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas)
print (valor_hora)