def MaxList():
    list1=[]
    n=int(input("Enter no of values"))
    for i in range(n):
        x=int(input())
        list1.append(x)
    print(list1)
    max=list1[0]
    j=1
    while j<n:
        if list1[j]>max:
            max=list1[j]
    j=j+1
    print("the maximum element in the list",max)
MaxList()




MaxList()