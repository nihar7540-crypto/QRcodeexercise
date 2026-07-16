b=int(input("enter a number: "))
if b%2==0:
    print("even")
elif b==0:
    print("nuetral")
else :
    print("odd")  

################################################

age=int(input("enter your age:"))
if age>=0 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("teenager")
elif age>=20 and age<=59:
    print("adult")
else:
    print("senior")    

################################################

for i in range(5):
    a=int(input("enter first number :"))
    b=int(input("enter secont number:"))
    c=int(input("enter third number :"))
    if a==b:
        print("a and b are equal")
        if c>a :
            print("c is greatest")
    elif a==c:
        print("a and c are equal")
        if b>a :
            print("c is greatest")
    elif b==c:
        print("c and b are equal")
        if a>b :
            print("c is greatest")
    elif a>b:
        if a>c:
            print("a is greatest")
        else:
            print("c is greatest")
    elif b>a:
        if b>c:
            print("b is greatest")
        else:
            print("c is greatest")
    elif a>c:
        if a>b:
            print("a is greatest")
        else:
            print("b is greatest")  
    else:
        print("all are equal")                  

#############################################

num=int(input("enter a number :"))
if num ==0:
    print("number is neutral")
elif num>0:
    print("positive")
else:
    print("negative")        

    