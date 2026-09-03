name = input("Enter your name:")

length = -len(name) - 1;
reverse_name = ""
for i in range(-1,length,-1):
    reverse_name += name[i]
    
print(f"Reversed name:{reverse_name}")