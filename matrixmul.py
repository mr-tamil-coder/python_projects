r=int(input("Enter number of rows"))
c=int(input("Enter number of columns"))
matOne=[]
print("Enter the elements of first matrix")
for i in range(r):
    matOne.append([])
    for j in range(c):
        num=int(input())
        matOne[i].append(num)
matTwo=[]
print("Enter the elements of second matrix")
for i in range(r):
    matTwo.append([])
    for j in range(c):
        num=int(input())
        matTwo[i].append(num)
matThree=[]
for i in range(len(matOne)):
    matThree.append([])
    for j in range(len(matOne[0])):
        mul=0
        for k in range(len(matTwo)):
            mul=mul+(matOne[i][k]*matTwo[k][j])
        matThree[i].append(mul)
print("The result of multiplication of matrix is ")
for i in range(r):
    for j in range(c):
        print(matThree[i][j],end=" ")
    print()
