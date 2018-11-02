if __name__ == '__main__':
    s = input()
    c=False
    for i in s:
       if i.isalnum():
            c=True
    print(c)
    c=False
    for i in s:
       if i.isalpha():
            c=True
    print(c)
    c=False
    for i in s:
       if i.isdigit():
            c=True
    print(c)
    c=False
    for i in s:
       if i.islower():
            c=True
    print(c)
    c=False
    for i in s:
       if i.isupper():
            c=True
    print(c)
        
   
