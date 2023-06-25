"""
2^3=2x2x2=8
2^1=2
"""

def power(base,exp):
    if exp==1:
        return base
    if exp!=1:
        return(base*power(base,exp-1))
base=int(input("Enter base:"))
exp=int(input("Enter exponential value"))
print("result: ",power(base,exp))