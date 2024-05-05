distance = float(input('What is the distance you are traveling in miles? '))
speed = float(input('What is the average speed in miles per hour at which you are going? '))
speedlimit = float (input('What is the average speed limit in miles per hour? '))

time = distance/speedlimit

speedtime= distance/speed

minutes_in_hour = 60

time_in_min = time*minutes_in_hour
speed_time_in_min = speedtime*minutes_in_hour

if speed > speedlimit:
    timesaved = time_in_min - speed_time_in_min
    print (f'Time saved is {timesaved}')
elif speed == speedlimit:
    print ('You are not speeding')
