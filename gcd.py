"""
10
20
1,2,5,10
1,2,5,10


1,2,5,10
"""

num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
if num1<num2:
    smaller=num1
else:
    smaller=num2
for i in range(1,smaller+1):
    if((num1%i==0) and (num2%i==0)):
        gcd=i
print("The G.C.D ",num1,"and",num2,"is =",gcd)