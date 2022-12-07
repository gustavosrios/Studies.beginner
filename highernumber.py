#condicionais if elfif else
#whats the higher number?
numero1 = input('Whats the first number?')
numero2 = input('Whats the second number?')
if int(numero1) < 0:
  print('The number one must be above zero')
  numero1 = input('Whats the first number?')
if int(numero2) < 0:
  print('The number two must be above zero')
  numero2 = input('Whats the second number?')
if numero1 > numero2:
  print('The first number is higher!')
if numero1 < numero2:
  print('The second number is higher!')
if numero1 == numero2:
  print('The numbers are equal, try again')

