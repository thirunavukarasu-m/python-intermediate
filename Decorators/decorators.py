def mydecorator(func):
    def wrapper(*args, **kwargs):
        print('============')
        return func(*args, **kwargs)
        print('============')
    return wrapper

   
@mydecorator
def do_something(name):
    print(f"{name}")
    return 5 + 5
    
print(do_something('Thiru'))


