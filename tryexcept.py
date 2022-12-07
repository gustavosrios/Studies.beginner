'''
while True:
  try:
    x = int(input('Number: '))
    print('Its the Number {}'.format(x))
    break
  except:
    print('\nThats not a valid entry!\nTry Again!')
  finally:
    print('Thats a valid number!')

  '''
def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as e: # AS E = COMO E  / VAI MOSTRAR O ERRO NO FORMAT(e)
      print("ZeroDivisionError occurred: {}".format(e))
      print("Insert another amout of people/cookies!")
    #except Exception as e:
      #print("Exception occurred: {}".format(e))
    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")