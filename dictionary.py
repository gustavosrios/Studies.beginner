
#A dictionary is a mutable data type that stores mappings of unique keys to values.
#its set with {} and the key can be int or float, dict_random = {'name': keyvalue}, {'name': keyvalue}... and so on.
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary and its written with [] = key, 
print("carbon" in elements) #check veracity return bool
print(elements.get("dilithium"))

#example self made dictionary 
product_price = {'rice': 15,'beans':  10,'meat': 100,'potatoes': 20, 'carrot': 10}
#product_price['grapple'] key error because its missing the : value
check_value = product_price.get('grapple')
print(check_value is product_price) # returns a bool
print(check_value is not product_price)
check_keyvalue = product_price.get('100')
print(check_keyvalue) #returns none because theres no 100 on the elements
print(product_price.get('tomato','This product isn\'t on the list!')) #returns my choice of answer since this element isnt found 

## Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8,'Istanbul': 13.3,'Karachi': 13.0,'Mumbai': 12.5}
# LISTS AS VALUES TO
animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
# print(animals[3]) key error
print(animals['cats'][5])


# invalid dictionary - this should break
room_numbers = {
    ('Freddie', 'Jen'): 403,
    ('Ned', 'Keith'): 391,
    ('Kristin', 'Jazzmyne'): 411,
    ('Eugene', 'Zach'): 395
}  #change [] to () making a tuple inside the dictionary
print(room_numbers)


# DICTIONARY INSIDE A DICTIONARY
elements = {"hydrogen": {"number": 1,"weight": 1.00794,"symbol": "H"},
            "helium": {"number": 2,"weight": 4.002602,"symbol": "He"}}
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print('elements = ', elements)
#create a key and a new dictionary inside elements dictionary
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H','is_noble_gas': False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He','is_noble_gas':True}}
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't