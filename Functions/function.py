def greet(name="User"):
    return f"Hello, {name}!"

def logger(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

logger("login", "success", user="admin", status="ok")

count = 0
msg = "jk"
def increment():
    global count
    count += 1

def outer():
    msg = "Hi"
    def inner():
        nonlocal msg
        msg = "Hello"
    inner()
    print(msg)
    return msg


increment()
print(outer())
print(msg)


names = ['a', 'b']
scores = [80, 90]
zipped = list(zip(names, scores))
print(zipped)

# Closures
def outer_1(msg):
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(f"Message: {msg}, {count}")
    return inner

say_hi = outer_1("Hi!")
say_hi()  # remembers msg = "Hi!"
say_hi()  # remembers msg = "Hi!"
say_hi()  # remembers msg = "Hi!"
say_hi()  # remembers msg = "Hi!"



def log(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def hello():
    print("Hello World!")

hello()
