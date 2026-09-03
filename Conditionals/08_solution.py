password = input("Enter your password:")
password_len = len(password)

if(password_len<6):
    print("Weak")
elif(6<=password_len<=10):
    print("Medium")
else:
    print("Strong")