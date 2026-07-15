for i in range(5):
    year=int(input("enter year to check: "))
    if year%400==0:
        if year%4==0:
            print ("this is a leap year")
        elif year%100==0:
            print("not a leap year")    
        else:
            print("not a leap year")    
    else:
        print("not a leap year")        
