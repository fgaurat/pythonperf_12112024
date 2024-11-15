from collections import deque

# HelloWorld = UpperCamelCase
# helloWorld = camelCase
# hello_world = snake_case
# hello-world = kebab-case
def main():
    l = [10,20,30,40,50]
    l.append(60)
    print(l)
    last_value = l.pop()
    print(l)
    print(last_value)
    l.insert(0,-10)
    print(l)
    first_value = l.pop(0)
    print(l)
    print(first_value)
    
    d = deque(l)
    print(d)
    d.appendleft(-10)
    print(d)
    
    print(l)
    
    
if __name__=='__main__':
    main()
