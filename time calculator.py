def main():
    seconds = int(input("Enter number of seconds: "))
    minute = int(seconds / 60)
    hour = int(seconds / 3600)
    day = int(seconds / 86400)

    if seconds >= 60:
        print(minute, "minute and" , seconds, "seconds")
    elif seconds <= 3600:
        print(hour, minute, "minute and", seconds, "seconds")
        else seconds >= 86400:
            print(day,"days", hour, "hour", minute, "minute and", seconds, "seconds")

main()
