def insert(list,n):
    for i in range(len(list)):
        if list[i]>n:
            index=i
            break
    list=list[:i]+[n]+list[i:]
    return list
list=[]
n=int(input("enter no of values"))
for i in range(n):
    x=int(input())
    list.append(x)
    list.sort()
n=int(input("enter noo of cards to be inserted"))
print(insert(list,n))

















'''def insert(sorted_list, n):
    i = len(sorted_list)
    for j in range(len(sorted_list)):
        if sorted_list[j] > n:
            i = j
            break
    sorted_list = sorted_list[:i] + [n] + sorted_list[i:]
    return sorted_list

list = []
n = int(input("Enter the number of values: "))
for i in range(n):
    x = int(input("Enter a value: "))
    list.append(x)

list.sort()  # No need to sort here

n = int(input("Enter the number of cards to be inserted: "))
print(list)
'''