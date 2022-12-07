# Tuples are a specific python strucuture, immutable and ordered that allows to store elements that are often used together like latitude and longitude, like length width and height 
'''
dimensions = 52, 40, 100 #tuple
length, width, height = dimensions # tuple unpacking
print("The dimensions are {} x {} x {}".format(length, width, height)) #posso usar format apos a parte de texto do print
'''
#write a program that recieves users height and weight and says his body mass index
tuple_a = 1, 2
tuple_b = (1, 2) 

print(tuple_a == tuple_b) #true, the parenthesis doesnt matter
print(tuple_a[1]) #prints number 1 index