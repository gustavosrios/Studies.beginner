'''
Identity Operators
Keyword	Operator
is - 	evaluates if both sides have the same identity
is not - 	evaluates if both sides have different identities

#example in a dictionary 

product_price = {'rice': 15,'beans':  10,'meat': 100,'potatoes': 20, 'carrot': 10}
check_value = product_price.get('grapple')
print(check_value is product_price) # returns a bool
print(check_value is not product_price)
'''

#QUIZ QUESTION
#What will the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) #true, b is equal to a, if i change A ill change B as well
print(a is b) #true a is identical to b, b is set equal to a
print(a == c) #true a has the same values as C, but can be false if i change the values of any
print(a is c) #false they are not the same, since c wasnt set equal to A
#course explanation -  List a and list b are equal and identical. List c is equal to a (and b for that matter) since they have the same contents. But a and c (and b for that matter, again) point to two different objects, i.e., they aren't identical objects. That is the difference between checking for equality vs. identity.