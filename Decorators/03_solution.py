def cache_decorator(func):
    cache = {}  # dictionary to store previous results

    def wrapper(*args, **kwargs):
        # make a key out of args + kwargs
        key = (args, frozenset(kwargs.items()))
        
        if key in cache:
            print("Returning cached result")
            return cache[key]
        
        # if not cached, execute and store result
        result = func(*args, **kwargs)
        cache[key] = result
        print("Function executed and result cached")
        return result

    return wrapper


@cache_decorator
def greet(name, age):
    print(f"Executing greet... Name = {name}, Age = {age}")
    return f"Greeting for {name}, {age}"


# Testing
print(greet("Ishu", 21))  
print(greet("Bovtlib", 21))  # cached
print(greet("Ishu", 22))  # new execution
print(greet("Bovtlib", 22))  # cached
