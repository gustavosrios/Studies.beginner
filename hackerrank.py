'''
if __name__ == '__main__':
    a = int(input('a:'))
    b = int(input('b:'))
    result01 = a // b
    result02 = float(a / b)

print(result01)
print(result02)

if __name__ == '__main__':
    n = int(input('n:'))
    count = 0
    if 1 <= n <= 20:
        for i in range(0,n):
            print(i ** 2)

def is_leap(year):
    leap = False
    
    # Write your logic here
    if 1900 <= year <= 10 ** 5:
        if year % 4 == 0:
            leap = True
        if year % 4 == 0 and year % 100 == 0:
            leap = False
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            leap = True
        
    
    return print(leap)

year = int(input('Year: '))
is_leap(year)

if __name__ == '__main__':
    n = int(input('n:'))
    phrase_number = ''   
    if 1 <= n <= 150:
        for i in range(1,n+1):
            phrase_number += str(i)
            #print(type(phrase_number))
print(phrase_number)

if __name__ == '__main__':
    n = int(input('score:'))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = 0                                          # MAIS TESTES

    for name, scores in student_marks.items():
        if 2 <= n <= 10:
            for i in scores:
                if  0 <= scores[i] <= 100 and len(scores) == 3:
                    result += scores[i]
print(result / 3)



def print_full_name(first, last):
    # Write your code here
    #phrase = f'Hello {first.title()} {last.title()}! You just delved into Python'
    return f'Hello {first.title()} {last.title()}! You just delved into Python'

if __name__ == '__main__':
    first_name = input('first name:')
    last_name = input('last name: ')
    print_full_name(first_name, last_name)

def mutate_string(string, position, character):
    string01 = list(string)
    string01[position] = character
    string = "".join(character)
    return 

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    print(string)

string = 'abracadabra'
position = 5
character = 'k'
mutate_string(string,position,character)

def count_substring(string, sub_string):
    counter = 0
    for i in range(0,len(string)):
        if 1 <= len(string) <= 200:
            if string[0]
            print(string.find(sub_string,i,len(sub_string)))        # tentar mais!!!!!!! slice[start:stop:step] step = len(sub_string)
            counter += 1
    return counter

if __name__ == '__main__':
    string = input('string: ').strip()
    sub_string = input('sub string:').strip()
    
    count = count_substring(string, sub_string)
    print(count)


testString1 = "Hello World!"
print("Original String: "+ testString1)


# Trying to slice out a substring between given indexes
print("Substring from index 1 to 7")
print(testString1[1:8])

#Substring from the start till character at index = 7 (start of string is index 0)
print ("Substring from the start till character at index = 7 (start of string is index 0): ")
print (testString1[:8])

#Substring from the character at index = 7, till the end of the string (remember: start of string is index 0)
print ("Substring from the character at index = 7, till the end of the string (remember: start of string is index 0): ")
print (testString1[7:])
'''
if __name__ == '__main__':
    N = int(input())
arr = []
def insert_list(i,e):
    arr.insert(i,e)
    return arr
def print_list():
    return print(arr)
def remove_e():
    arr.pop(0) 
def append_num(num_int,position):
    arr.append(num_int[position])
    return arr

 

    return arr
def sort():
    arr.sort()
    return arr

def reverse():
    arr.reverse()
    return arr


    # runner up score
    #  # preciso de atribuir dois contsdores, quando o loop chegar no ultimo iterado ele so entrara a condicional no primeiro contador o segundo permanecera sem modificar e sera o segundo lugar