import time
def get_minutes():
    while True:
        try:
            stop_min = int(input('Enter time in minutes between 5 and 25: '))
            
        except ValueError:
            print("The input should be an integer between 5 and 25")
            continue
        else:
            if 5 <= stop_min <= 25:
                return stop_min
            else:
                print("We needed a number between 5 and 25. Please try again")
            
def timer(minutes):
    time_mins = 0
    print(f'The timer for {minutes} minutes starts now')
    while time_mins != minutes:
        print(">" * time_mins)
        time.sleep(60)
        time_mins += 1
    print(f'Your timer for {minutes} minute(s) is done')


current_time = time.strftime('%a %H:%M:%S')
print(f'Hello. Right now it is {current_time}.')
user_minutes = get_minutes()
timer(user_minutes)




