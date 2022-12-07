'''
this script inputs an integer and returns its square
'''
def ask():
    '''this function is named ask, for inputs'''
    while True:
        try:
            input_int = int(input('Integer number: '))
            print(f'Thank you, your number squared is: {input_int**2}')
            break
        except TypeError:
            print('An error occurred! Please try again!')
            continue
        except ValueError:
            print('An error occurred! Please try again!')
            continue
while True:
    try:
        ask()
        keep_asking = input('Continue? (y/n): ')
        if keep_asking.lower() == 'y':
            continue
        if keep_asking.lower() == 'n':
            break
        if keep_asking.lower() != 'n' and keep_asking.lower() != 'y':
            print('Invalid input')
            break
    except TypeError:
        print('An error occurred! Please try again!')
        continue
    except ValueError:
        print('An error occurred! Please try again!')
        continue
