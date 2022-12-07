'''
#write a program that recieves a lists of names and returns how many names are equal, even the surnames are valid *self-thought exercices*
user_list01 = []
list01_end = False
often_times = 0
print('Welcome, here you type list of names and we tell you what name is more often seen!')
while list01_end == False:
  list01_name = input('Type the first name: ')
  user_list01.append(list01_name)
  list01_surname = input('Type the surname: ')
  user_list01.append(list01_surname)
  add_more = input("Do you want to add more names?: (Y/N)").upper()
  if add_more == ('Y'):
    list01_name = input('Type the first name: ')
    user_list01.append(list01_name)
    list01_surname = input('Type the surname: ')
    user_list01.append(list01_surname)
    add_more = input("Do you want to add more names?: (Y/N)").upper()
  elif add_more == ('N'):
    list01_end = True
print('The list is done! Calculating results...')
for check_name,check_surname in zip(user_list01,user_list01[1:]):
  if str(check_name) == str(check_surname):
    often_times += 1
    winner.check
    print('The name:',,'Is been said for:',often_times)
    '''

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print([len(a),len(b),len(c)])
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))