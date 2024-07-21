

#very basic decorator
#def degug(func):
#    def wrapper():
#        print("hello world")
#        return func()
#    
#    return wrapper
#@degug
#def hello():
#    print("hello")
#
#hello()  



def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"Calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)

    return wrapper

@debug
def hello():
    print("hello")
 


@debug
def greet(name,greeting="Namaste"):
    print(f"{greeting} ,{name}")

hello()    
greet("dadaji",greeting="Namaste")    
    