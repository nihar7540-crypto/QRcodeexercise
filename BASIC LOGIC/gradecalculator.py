# 90+ : A
# 80–89 : B
# 70–79 : C
# 60–69 : D
# Below 60 : F

for i in range(5):
    grade=int (input("enter your grade out of 100:"))
    if grade >100:
        print("invalid input")
    elif grade<=100:
        if grade>=90:
            print("A grade")    
        elif grade>=80 and grade<=89:
            print("B grade")
        elif grade>=70 and grade<=79:
            print("C grade") 
        elif grade>=60 and grade<=69:
            print("D grade")  
        else:
            print("F grade")    