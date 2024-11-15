import timeit
def init_loop():
    r = []
    for i in range(100):
        r.append(i)

def init_map():
    r = list(map(lambda i:i,range(100)))

def init_comp():
    r = [i for i in range(100)]
    
    
def main():
    t1 = timeit.timeit(init_loop)
    t2 = timeit.timeit(init_map)
    t3 = timeit.timeit(init_comp)
    print(t1)
    print(t2)
    print(t3)
if __name__=='__main__':
    main()
