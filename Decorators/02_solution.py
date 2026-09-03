def decorator(func):
    def wrapper(*args,**kwargs):
        l1 = len(args)
        l2 = len(kwargs)
        result = func(*args,**kwargs)
        print(f"No. of arguments:{l1+l2} \nCalling function name:{func.__name__}")
        return result
    return wrapper

@decorator
def greet(name,number,greeting = "Namaste"):
    print(f"{greeting} , {name}")

greet("Mau",2,greeting="Hanji")