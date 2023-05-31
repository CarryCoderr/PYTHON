x=range(0,21,5)
for i in x:
    print(i)
for i in range(1,11):
    print(i)
num=int(input("enter the number"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)
n=7
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end =" ")
    print("\n")