#condicionais
# Lets hang out! only if i had finished the job!

trabalho_terminado = input('Lets hang out today at midnight?')
verificar_trabalho = bool
if trabalho_terminado == str('Yes'):
  verificar_trabalho = True
if trabalho_terminado == str('No'):
  verificar_trabalho = False
if verificar_trabalho == True:
  print('Yes find me at 10pm')
else:
    print('havent finished the job yet, i call you when its done')