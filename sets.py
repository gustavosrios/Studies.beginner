# A set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list.
# Write a program that recieves multiples users name and delete their duplicates
names_end = False
names_list = []
name = (input('Type your name: '))
while names_end == False:
  if name == (int, float, bool):
    print('Only alphabetic characters are allowed for names!')
    name = (input('Type your name: '))
  else:
    names_list.append(name)
  add_new = (input('Want to add new names? (y/n)'))
  if add_new.lower() == ('y'):
    name = (input('Type your name: '))
    if name == (int, float, bool):
      print('Only alphabetic characters are allowed for names!')
      name = (input('Type your name: '))
      names_list.append(name)
  elif add_new.lower() == ('n'):
    names_end = True
names_list = set(names_list)
print(names_list)

names_list.add('paula')
print(names_list)
