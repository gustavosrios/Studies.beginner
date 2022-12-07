def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name

#Quiz: Population Density Function
#Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values. I've included two test cases that you can use to verify that your function works correctly. Once you've written your function, use the Test Run button to test your code.
# write your function here
def population_density(population,land_area):
  x = population / land_area
  return x
# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

#Quiz: readable_timedelta
#Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:
#print(readable_timedelta(10)) should output the following:
#1 week(s) and 3 day(s).
def readable_timedelta(days):
  if days <= 7 :
    weeks = 0
    return print('{} week(s) and {} days(s)'.format(weeks,days))
  else:
    weeks = days // 7
    day = days - (weeks * 7)
    return print('{} week(s) and {} days(s)'.format(weeks,day))
print(readable_timedelta(10))

#exercice
def some_function():
  word = "hello"
  return word
x = some_function()
print(x)

