num=int(input("enter the number"))
count=1;
print("the multiplication table of", num)
while count<=10:
    num=num*1
    print(num,'x',count,'=',num*count)
    count+=1
total=0
num1=int(input("enter the number"))
while num1 !=0:
    total+=num1
    num1=int(input('enter a number'))
print('total=',total)
##
n=int(input("enter the number"))
i=1
while i<=n :
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1