# Write a program that recieves your mother year of birthday and the age she was when you've been born and tells you the year you've been born
mother_year = int(input('Whats the year your mother has been born?: '))
mother_age = int(input('Whats the age your mother was when you\'ve been born?:'))
user_year = mother_year + mother_age
print('The year you\'ve been born it\'s your mothers year of birthday plus the age she was when you\'ve been born:',user_year)