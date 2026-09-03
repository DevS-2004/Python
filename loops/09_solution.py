items = ["apple", "banana", "orange", "apple", "mango"]

for fruit in items:
    if(items.count(fruit)>1):
        print(f"Duplicate fruit : {fruit}")
        break
else:
    print("No duplicate fruit is found!!")