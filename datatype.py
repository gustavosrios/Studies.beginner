# the types are defined as class  - integer(int), string(str), float(float), boolean(bool)

# Write a program that recieves a registration, and prints the types of the data recieved
print("Hello! This is the 0.0001v of the registration program!")
name = input("Name: ")
print("Hello,",name,"Now we will need your personal information!")
birth_date = input("Date of birth: ")
profession = input("Profession: ")
birth_place = input("Country of origin: ")
print("Now your address, note that it will start asking the country and end asking the number of your house.")
country = input("Country you live at the moment: ")
city = input("City: ")
district = input("District: ")
street = input("Street: ")
number = int(input("Number:"))
print("So you want to study...Let me check out what you want! Type Yes or No!")
tastes_01 = input("You like Python?")
if tastes_01 == ("Yes"):
  tastes_01 = True
  print("Not bad!")
  tastes_02 = input("You want learn more?")
  if tastes_02 == ("Yes"):
    tastes_02 = True
    print("We/'ve got some good courses for you!")
  if tastes_02 == ("No"):
    tastes_02 = False
    print("We\'re here to provide knowledge of Python, if become interested come back again, maybe you can find some new version of me! =D")
else:
  print("We\'re here to provide knowledge of Python, if become interested come here again, maybe you can find some new version of me! =D")

print("Thats all we needed for the moment thank you for taking your time and registering!")
print(type(birth_date))
print(type(profession))
print(type(birth_place))
print(type(country))
print(type(city))
print(type(district))
print(type(street))
print(type(number))
print(type(tastes_01))
print(type(tastes_02))