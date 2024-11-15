def make_incrementor(i):
    
    def f(j):
        return i+j
    
    return f

def main():
    do_inc = make_incrementor(10)
    r = do_inc(5)
    print(r) # 15
    r = do_inc(12)
    print(r) # 22

if __name__=='__main__':
    main()
