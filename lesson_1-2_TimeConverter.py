time = input("Enter time in seconds: ")
if not time.isdecimal():
    print("It's a wrong time.")
else:
    time = int(time)
    if time >= 86400:
        print("It is more than one day. Try again")
    else:
        hour = time // 3600
        minutes = time % 3600 // 60
        seconds = time % 3600 % 60
        print(f"It's {hour:02}:{minutes:02}:{seconds:02}")
