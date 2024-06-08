# a) Basic Calculator Questtion 1

while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    ch = int(input("Enter Choice(1-5):"))
    if ch == 5:
        print("Exiting the Calculator")
        break
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    if ch == 1:
        print("Addition:",(num1+num2))
    elif ch == 2:        
        print("Substraction:",(num1-num2))
    elif ch == 3:        
        print("Multiplication:",(num1*num2))
    elif ch == 4:        
        print("Division:",(num1/num2))
    else:
        print("Invalid Choice")
    continue_ch = input("Do you want to continue?(yes/no)")
    if continue_ch != "yes":
        print("Exiting the calculator")
        break