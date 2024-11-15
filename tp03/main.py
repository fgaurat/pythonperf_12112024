import traceback
class DivBy12Error(Exception):
    
    def __init__(self):
        super().__init__("Division par 12")

def div(a,b):
    if b==12:
        raise DivBy12Error()
    return a/b


def call_div(a,b):
    try:
        print("OPEN")
        r = div(a,b)
    finally:
        print("CLOSE")
    return r


def main():
    try:
        a = 2
        b = int(input('b:'))
        c =call_div(a,b)
        print(c)
    except DivBy12Error as e:
        print("DivBy12Error",e)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print("Erreur",e)
        # traceback.print_exc()
    except Exception as e:
        print("Exception",e)
    else:
        print("pas d'erreur")
    
    print("la suite")
if __name__=='__main__':
    main()
