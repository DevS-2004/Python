text = input("Enter any text : ")

for char in text:
    if(text.count(char)==1):
        print(f"First non-repeated character {char}")
        break
else:
    print("Non-repeated character found!!")
