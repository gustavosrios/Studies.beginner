'''
#num_list = [num for num in range(100) if num > 0] 
#print(num_list)
#code_list = [code * 2 for code in range(100) if code > 0 and code < 70]
#print(code_list)
#python = 'Python'
#study_list = [python * 2 for num in range(10)]
#print(study_list)
#squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

#Quiz: Extract First Names
#Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# criar a lista first_names com os nomes minusculos, separados as palavras, e apenas a posicao [0] delas, ['Rick'] = [0], ['Morty'] = [0]
first_names = [name.lower().split()[0] for name in names] 
# write your list comprehension here
print(first_names)


#list with the 20 first multiples of 3
multiples_3 = [num for num in range(1,63) if num % 3 == 0 ]
print(multiples_3)
'''

#Quiz: Filter Names by Scores
#Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name in scores if scores.get(name) > 65]
print(passed)