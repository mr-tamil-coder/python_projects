'''formula
approx=0.5*n
better=0.5*(approx+n/approx)
'''
def newton(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while approx!=better:
        approx=better

        better = 0.5 * (approx + n / approx)
    return approx
n=int(input("Enter number"))
print("the sqrt of number is ",newton(n))