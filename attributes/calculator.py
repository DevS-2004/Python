def add(*args):
    return args[0] + args[1]

if __name__== "__main__":
    print("Starting calculator..")
    ans = add(5,6)
    print("Sum: ",ans)

print(__name__)