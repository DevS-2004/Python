def bold(func):
    # @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet_html():
    return "Hello"

print(greet_html.__name__)
print(greet_html())  # <b><i>Hello</i></b>