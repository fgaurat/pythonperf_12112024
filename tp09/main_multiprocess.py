from multiprocessing import Pool
import os
import time

def slow_f(x):
    start = time.time()
    t=1
    while time.time() - start<t:
        pass
    
    return x*x

def f(x):
    return x*x

def main():
    print(os.cpu_count())
    with Pool(2) as p:
        print(p.map(slow_f, range(100)))

if __name__=='__main__':
    main()
