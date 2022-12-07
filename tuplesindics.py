# write a program that recieved tuples of data inside a dictionary
# NAME surname : age, with the search of age based on the name or surname input
tuple_end = False
name_dict = {}
while tuple_end == False: 
  name = input('Type your name: ')
  surname = input('Type your surname: ')
  age = int(input('Type your age: '))
  name_dict[name,surname] = age
  add_more = str(input('You want add other people? (Y/N)'))
  if add_more == ('Y'):
    name = input('Type your name: ')
    surname = input('Type your surname: ')
    age = int(input('Type your age: '))
    name_dict[name,surname] = age # FORM TO USE NAME AND SURNAME AS KEY AND SET AGE AS VAUE
    add_more = str(input('You want add other people? (Y/N)'))
  if add_more == ('N'):
    tuple_end = True
print(name_dict)
'''
# CHECKING NAMES FUNCTION MORE KNOWLEDGE REQUIRED
check_name = input('Type a name to check its age:')
name_dict.get(check_name)
''' 