def check(n):
    print(f"Even numbers upto {n}")
    for i in range(1,n+1):
        if(i%2==0): print(f"{i}",end=" ")


check(10)