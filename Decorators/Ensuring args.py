'''from functools import wraps
#Another Example Ensuring Args With A Decorator
def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sorry :(")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hi There {name}")

greet(name="Rani")'''


# NOT WORKING CODE!
# JUST FOR DEMO PURPOSES!

# When we write:
'''@decorator
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator(func)


# When we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator_with_args(arg)(func)'''



def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a,b):
    print(a/b)
# repeat_msg("hello", '5')
divide('1', '4')

