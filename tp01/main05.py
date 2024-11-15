def add(*args):
    print(args)
    r = sum(args)
    return r

def hello(**kwargs):
    print(kwargs)

def hello2(name,firstName,/):
    print(name,firstName)

def hello3(*,name,firstName):
    print(name,firstName)
    
    
def main():
    l = [10,20,30,40,50]
    r = add(*l) 
    # print(r) # 150
    
    r = add(10,20,30,40,50) 
    print(r) # 150

    a,b,*lereste = 0,1,3,5,8
    print(a,b,lereste)
    
    print(l)
    print(*l)
    # print(10,20,30,40,50) 
    hello(firstName="Fred",name="GAURAT",job="dev")
    hello2("Fred","GAURAT")
    hello3(firstName="Fred",name="GAURAT")
    print(50*'-')
    a=2
    b=3
    c = a/b
    r  =f"{a=}, {b=} {c:.2%}"
    print(r)    
    
    r  ="{0} {1} = {2:.2%}".format(a,b,c)
    l = [a,b,c]
    r  ="{0} {1} = {2:.2%}".format(*l)
    print(r)   
    name="GAURAT" 
    firstName="Fred"
   
    d = {
        "name":"GAURAT", 
        "firstName":"Fred"
        
    }
    r  ="Bonjour {theName} {theFirstName}".format(theName=name, theFirstName=firstName)
    r  ="Bonjour {name} {firstName}".format(name=name, firstName=firstName)
    r  ="Bonjour {name} {firstName}".format(**d)
    
    print(r)   
    
    p = r"c:\new_project\test"
    print(p)
     
if __name__=='__main__':
    main()
