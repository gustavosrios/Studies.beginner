'''
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Write a for loop to print out each word in the sentence list, one word per line
for i in range(0, len(sentence)):
    print(sentence[i])
#for word in sentence:
    print(word)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for i in range(5, 35, 5):
    print(i)

#Quiz: Create Usernames
#Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in range(len(names)):
    names[name] = names[name].replace(' ','_')
    names[name] = names[name].lower()
    user_names.append(names[name])
# OU melhor resposta 
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

#Quiz: Modify Usernames with Range
Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for name in range(len(usernames)):
    usernames[name] = usernames[name].lower()
    usernames[name] = usernames[name].replace(' ','_')

print(usernames)

#Quiz: Tag Counter
#Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for name in range(len(tokens)):
    if tokens[name].count('<' or '>'):
      count += 1
#MELHOR RESPOSTA
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)

# <ul>
#<li>first string</li>
#<li>second string</li>
#</ul>
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does                     
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
  html_str = html_str + "<li>" + str(item) + "</li>" "\n" #
html_str = html_str + "</ul>"
print(html_str)
#MELHOR RESPOSTA
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(list(range(4)))  #sempre -1 pro final
print(list(range(0,-5))) #sai [] pois -5 nao eh um final valido
print(list(range(4,10,2))) #do 4 ao 8 pulando de 2 em 2

#print a new list with all colors in lower case
colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = []

for color in colors:
  lower_colors.append(color.lower()) #pegar cada colors[color], inserir em lower_colors(com letra minuscula)
print(lower_colors)
'''