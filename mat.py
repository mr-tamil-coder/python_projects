r=int(input("row"))
c=int(input("column"))
matOne=[]
print("first element")
for i in range(r):
    matOne.append([])
    for j in range(c):
        num=int(input())
        matOne[i].append(num)

matTwo=[]
print("first element")
for i in range(r):
    matTwo.append([])
    for j in range(c):
        num=int(input())
        matTwo[i].append(num)
matThree=[]
for i in range(len(matOne)):
    matThree.append([])
    for j in range(len(matTwo[0])):
        sum=0
        for k in range(len(matTwo)):
            sum=sum+(matOne[i][k]*matTwo[k][j])
        matThree[i].append(sum)

for i in range(r):
    for j in range(c):
        print(matThree[i][j],end=" ")
    print()

