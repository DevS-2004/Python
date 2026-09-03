n = int(input("Value of n:"))
ans = 0;

for num in range(n+1):
    if(num%2==0):
        ans += num
print(f"Sum of even number upto {n}:{ans}")