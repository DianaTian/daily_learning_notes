def computepay(hours, rate):
    try:
        hours = float(input("Enter hours: "))
    except:
        print("Error, please enter numeric input")
        exit()

    try:
        rate = float(input("Enter Rate: "))
    except:
        print("Error, please enter numeric input")
        exit()

    if hours > 40:
        extra = hours - 40
        print("Pay: ", (40 + extra * 1.5) * rate)
    else:
        print("Pay: ", hours * rate)

computepay(45, 10)