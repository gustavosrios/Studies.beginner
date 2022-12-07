# Write a program that recieves the users car speed in a 80km/h road, if hes below 80km/h notify that theres no fine, if hes above 10km/h from the maximum notify that he got a light traffic fine, if hes between 11km/h to 20km/h from the maximum notify that he got a medium traffic fine, and lastly if hes above 20km/h he got the heavy traffic fine
car_speed = int(input('Whats the speed of your car now?'))
if car_speed <= 80:
  print('Equal or Below 80km/h. No Traffic Fine.')
if car_speed > 80:
    if car_speed < 90:
      print('Your car speed is between 80km/h to 90km/h. Lesser Traffic Fine.')
if car_speed > 91:
  if car_speed < 100:
    print('Your car speed is between 91km/h to 100km/h, Medium Trafic Fine.')
if car_speed > 100:
  print('Your car speed is above 100km/h.Heavy Traffic Fine.')