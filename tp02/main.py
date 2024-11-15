from functools import wraps


def do_log(log_file):
    def decorator(func):
        
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('LOG param to ',log_file,*args,kwargs.values(),func)
            r = func(*args,**kwargs)
            print(func)
            print('LOG return',log_file,r)
            return r
        return wrapper 
    return decorator

@do_log("thelog.log")
def say_hello(name,job):
    """Docstring"""
    r = f"Hello {name}"
    print("write file")
    return r

def main():
    r = say_hello("fred",job="dev")
    print(r)
    print(50*'-')
    print(say_hello.__name__)
    print(say_hello.__doc__)



if __name__=='__main__':
    main()
