def old_mult2(l):
    r = []
    for i in l:
        r.append(i*2)
    return r

def mult2(i):
    return i*2
 
def main():
    l = [10,20,30,40,50]
    # l2 = mult2(l)
    # print(l2) # [20,40,60,80,100]
    
    # l2 = list(map(mult2,l))
    lmb = lambda i:i*2
    l2 = list(map(lmb ,l))
    print(l2) # [20,40,60,80,100]
    l2 = [i*2 for i in l]
    print(l2)
if __name__=='__main__':
    main()
