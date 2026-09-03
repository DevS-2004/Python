n = int(input("Value of n:"))

ans = 1
for i in range(1,n+1):
    ans *= i
print(f"Factorial of {n} : {ans}")