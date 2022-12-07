class Car():
    def __init__(self,model,year,color,power,km_mark,rent_price):
        self.model = model
        self.year = int(year)
        self.color = color
        self.power = float(power)
        self.km_mark = float(km_mark)
        self.rent_price = int(rent_price)
car_list = [] 
def identifier():
    while True:
        try:
            identify = input('Hello! Customer or Admin or Exit?')
            if identify.lower() == 'customer' or identify.lower() == 'admin' or identify.lower() == 'exit':
                break
            else:
                print('Invalid input')
                continue
        except:
            print('Invalid input')
    return identify.lower()
def adm_user():
    global car_list
    print('Welcome Admin. Here you can add new cars.')
    while True:
        model_input = input('Model: ')
        year_input = int(input('Year: '))
        color_input = input('Color: ')
        power_input = float(input('Power: '))
        km_input = int(input('KM: '))
        rent_input = int(input('Rent Value per Day: '))
        car = Car(model_input,year_input,color_input,power_input,
                  km_input,rent_input)
        car_list.append(car)
        add_more = input('Add car? (y/n) ')
        if add_more.lower() == 'y':
            display_cars()
            continue
        else:
            display_cars()
            break
def display_cars(): 
    global car_list
    print(f'        Model\tYear\tColor\tPower\tKM\t\tRent Price')
    i = 0
    for car in car_list:
        print(f'Car {i}   {car.model:<1}\t{car.year:^1}\t{car.color:^1}\t{car.power:^1}\t{car.km_mark:^1}\t\t{car.rent_price:>1}')
        i += 1
def customer():
    global car_list
    print(f'Welcome to the car rent!')
    print('Heres a list of our available cars!')
    display_cars()
    choice = input('Did you find any of your preference (Car model/number of the car?)')
    if choice.isdigit():
        print(f'Your choice: {car_list[int(choice)].model}')
        print(f'The rent price is {car_list[int(choice)].rent_price}/day')
        days = int(input('Choose how many days: '))
        if days >= 30:
            print(f'30% discount!\nCalculating Price...')
            total = (car_list[int(choice)].rent_price) * days - (car_list[int(choice)].rent_price * days * 0.30)
            print(f'Total: {total}')
        elif days >= 10:
            print(f'10% discount!\nCalculating Price...')
            total = (car_list[int(choice)].rent_price) * days - (car_list[int(choice)].rent_price * days * 0.10)
            print(f'Total: {total}')
        else: 
            total = (car_list[int(choice)].rent_price) * days
            print(f'Total: {total}')
    elif choice.isalpha():
        for car in car_list:
            if choice.lower() == car.model:
                chosen_car = car.model
                chosen_price = car.rent_price
            else:
                continue
        print(f'Your choice: {chosen_car}')
        days = int(input('Choose how many days: '))
        if days >= 30:
            print(f'30% discount!\nCalculating Price...')
            total = (chosen_price * days) - (chosen_price * days * 0.30)
            print(f'Total: {total}')
        elif days >= 10:
            print(f'10% discount!\nCalculating Price...')
            total = (chosen_price * days) - (chosen_price * days * 0.10)
            print(f'Total: {total}')    
        else:
            total = (chosen_price * days)
            print(f'Total: {total}')                              
def main():
    while True:
        user = identifier()
        if user == 'admin':
            adm_user()
            continue
        if user == 'customer':   
            customer()
            continue
        if user == 'exit':
            break
main()