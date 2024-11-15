def main():
    l = [10,20,30,40,50]
    
    to_found = 300
    
    for i in l:
        if i == to_found:
            print("ok")
            break
    else:
        print("ko")
if __name__=='__main__':
    main()
