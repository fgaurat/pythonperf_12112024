import sys

def main():
    print('Hello')
    a = 2
    b = 2
    print("a",hex(id(a)))
    print("b",hex(id(b)))
    a = 3
    print(hex(id(a)))
    
    print("getrefcount",sys.getrefcount(1598455648745))
    a = 1598455648745
    print("getrefcount",sys.getrefcount(1598455648745))
if __name__=='__main__':
    main()
