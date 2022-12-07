#condicionais 02
'''
got late for the class can i still join? if its not the third time arriving late you can but if its you are suspended!
'''
numero_de_atrasos = input('How many times have you arrived late for class?')
if int(numero_de_atrasos) <= 3:
  print('You can join us')
else:
  print('You arrived more then three times late, so you are now suspended!')
if int(numero_de_atrasos) == 3:
  print('This is the last time you can join us this late!')
if int(numero_de_atrasos) == 2:
  print('Caution! You have only one more delay until suspension')
if int(numero_de_atrasos) == 1:
  print('Take care! You only have two more delays until suspension!')
if int(numero_de_atrasos) == 0:
  print('This is your first delay, you will be suspended only after 3 delays')