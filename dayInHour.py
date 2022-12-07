#def convert_day(day) as f:
#input_list = [] 
input_time = input('Say the time using the format day-hour-minute-second')
show_hour = list(input_time.split('-'))
#print(show_hour)
#print(input_time)
for i in range(0,len(show_hour)):
    total_hour = (int(show_hour[i]) * 24) + (int(show_hour[i+1]))
    print(f'The time in hours is {total_hour}:{show_hour[i+2]}:{show_hour[i+3]}')

