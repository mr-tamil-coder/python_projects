print("Simple Calculator")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.modulus")
print("6.exponential")

while True:
    choice=input("Enter choice: [1,2,3,4,5,6] ")
    if choice in ('1','2','3','4','5','6'):
        try:
            num1= int(input("Enter first number"))
            num2 = int(input("Enter second number"))
        except ValueError:
            print("please enter integer ")
            continue

        if choice=="1":
            print("the additon of two number is ",num1+num2)
        elif choice=='2':
            print("the subtraction of two number is ", num1 - num2)
        elif choice == '3':
            print("the multiplication of two number is ", num1 * num2)
        elif choice == '4':
            print("the division of two number is ",num1/num2)
        elif choice=='5':
            print("the modulus of two number is ",num1%num2)
        elif choice=='6':
            print("the exponential of two number is ", num1 ** num2)
        want=input("Do you want again calculations ?(yes/no)")
        if want=='no':
            break





















