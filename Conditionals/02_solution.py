age = int(input("Enter your age: "))
day = input("Enter day to watch movie :").lower()

if (age >18):
    if (day == "wednesday"):
        print("Ticket price :",10);
    else:
        print("Ticket Price :",12)
else:
    if (day == "wednesday"):
        print("Ticket price :",6);
    else:
        print("Ticket Price :",8)