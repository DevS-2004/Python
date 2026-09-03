def dictionary(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} -> {value}")

dictionary(name="Devendra",age=21,Gender="Male")