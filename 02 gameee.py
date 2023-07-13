"""
user 1-10
rand 5

"""
import random
start=int(input("Enter starting range "))
end=int(input("Enter starting range "))
rand=random.randint(start,end)
while True:
    print("Guess a number between ",start,"and",end)
    user=int(input())
    if user==rand:
        print("Congratulations You Won")
        break
    elif user>rand:
        print("too high")
    elif user<rand:
        print("too low")
    
def rand:
mport random
start=int(input("Enter starting range "))
end=int(input("Enter starting range "))
rand=random.randint(start,end)
while True:
    print("Guess a number between ",start,"and",end)
    user=int(input())
    if user==rand:
        print("Congratulations You Won")
        break
    elif user>rand:
        print("too high")
    elif user<rand:
