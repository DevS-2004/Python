n = int(input("Enter value of n:"))

print("Multiplication table (except fifth position)")
for multiplier in range(1,11):
    if(multiplier==5):
        pass
    else:
        print(f"{n}x{multiplier}:{n*multiplier}")
