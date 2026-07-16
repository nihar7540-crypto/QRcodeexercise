for i in range(5):
    a=int(input("enter first number :"))
    b=int(input("enter secont number:"))
    c=int(input("enter third number :"))
    if a==b:
        print("a and b are equal")
        if c>a :
            print("a and b are smallest")
        else:
            print("c is smallest")    
    elif a==c:
        print("a and c are equal")
        if b>a :
            print("a and c is smallest")
        else:
            print("b is smallest")    
    elif b==c:
        print("c and b are equal")
        if a>b :
            print("c and b are smallest")
        else:
            print("a is smallest")    
    elif a<b:
        if a<c:
            print("a is smallest")
        else:
            print("c is smallest")
    elif b<a:
        if b<c:
            print("b is smallest")
        else:
            print("c is smallest")
    elif a<c:
        if a<b:
            print("a is smallest")
        else:
            print("b is smallest")  
    else:
        print("all are equal") 