import copy

def main():
    l = [10,20,30,40,50]
    print(l[2:4])
    print(l[:2],l[2:])
    print(l[:])
    # l1 = l.copy()
    # l1 = copy.copy(l)
    l1 = l[:]
    l[0] = 1000
    print(l)
    print(l1)
    
    l= [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]
    l1 = copy.deepcopy(l)
    l[1][1] = 1000
    print(l)
    print(l1)
    
if __name__=='__main__':
    main()
