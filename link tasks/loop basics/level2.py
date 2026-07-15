for i in range (1,100+1):
    if i%3==0:
        print(i)

##################################################

for i in range(1,100+1):
    if i%3==0:
        if i%5==0:
            print(i)

##################################################

counteven=0
for i in range(1,50+1):
    if i%2==0:
        counteven+=1
print(counteven)

##################################################

divby7=0
n=int(input("enter a number: "))
for i in range(1,n+1):
    if i%7==0:
        divby7+=1
print(divby7)

##################################################

n=int(input("enter a number: "))
for i in range(1,n+1):
    if i%2!=0:
        print(i)

