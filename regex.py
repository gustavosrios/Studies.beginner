import re
phone_text = 'My phone is (055) 99455-4431, my old phone were (099) 99999-8888'
pattern = 'phone'
#match = re.search(pattern,phone_text)
all_matches = re.findall('phone',phone_text)
print(all_matches)
for match in re.finditer(pattern, phone_text):
    print(match)
    print(match.span())
    print(match.group())


text = 'Thats the office number (054) 99664-5566'
phone_finder = re.search(r"\W\d{3}\W\s\d{5}-\d{4}",text)
#phone_finder.group()
phone_pattern = re.compile(r'(\W\d{3}\W\s)(\d{5})-(\d{4})') #compile divide ()()() grupos de patterns (1)(2)(3)
result = re.search(phone_pattern,text)
result.group()
result.group(1)


re.search(r'cat|dog','The cat is here')
re.findall(r'.at','The cat is here') #search for one word+at / .. two words ... three words
re.findall(r'^\d','2 is a number') #search digit at beginning
re.findall(r'\d$','The number is 2') # search digit at end
phrase = 'There are 3 numbers 34 inside this 5 sentence'
pattern =  r'[^\d]+' # [^excludes digits] + return all words at the same list
re.findall(pattern,phrase)
phrase2 = 'This is a string! But it has punctuation.How can we remove it?'
clean_phrase2 = re.findall(r'[^!.?]+',phrase2) #exclui todos simbolos pontos
' '.join(clean_phrase2)


text_a= 'Only find the hypen-words in this sentence.But you dont know how long-ish they are'
#re.findall(r'[^\w]+',text)
pattern = r'[\w]+-[\w]+'
re.findall(pattern,text_a)


text_01 = 'Hello, would you like some catfish?'
text_02 = 'Hello, would you like to take a catnap?'
text_03 = 'Hello, have you seen this caterpillar?'
re.search(r'cat(fish|nap|erpillar)',text_01)
re.search(r'cat(fish|nap|erpillar)',text_02)
re.search(r'cat(fish|nap|erpillar)',text_03)