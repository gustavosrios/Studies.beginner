'''p_drome = input('Type a word:')
count = -1
palin_check = True
for letter in p_drome:
  if letter != p_drome[count]:
    palin_check = False
    break
  else:
    count -= 1
if palin_check == False:
  print('Not a palindrome')
else:
  print('its a palindrome')
  
  
  #new_word = letter.find(p_drome)
  
  #print(new_word)
  #print('letter:')
  #print(letter)
  
  #p_check = p_drome[len(p_drome):-1]
  #print(p_check)
  '''
  #slice way
p_drome = input('Type a word:')
if p_drome[0:len(p_drome)] == p_drome[::-1]:
  print(f'{p_drome}\tIts a palindrome!')
else:
  print(f'{p_drome}\tIts not a palindrome!')