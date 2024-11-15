import lib as lb
from lib import hello as hl

def hello():
    print("Hello from main")
    
    
a = 2
def main():
    global a
    
    a=158
    # lb.hello()
    hello()
    # hl()
    print("in",a)
    print(lb.the_var)
if __name__=='__main__':
    print("before",a)
    main()
    print("after",a)
