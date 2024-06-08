# b) Temperature Conversion Tool Question no 2

while True:
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.Exit")
    ch = int(input("Enter choice:"))
    if ch == 3:
        print("Exiting the Calculator")
        break
    if ch == 1:
        C = int(input("Enter temperature in Celsius:"))
        F = (9/5)*C+32
        print("Celsius to Fahrenheit is ",F)
    elif ch == 2:
        F = int(input("Enter temperature in Fahrenheit:"))
        C = (F-32)*5/9
        print("Fahrenheit to Celsius is ",C)
    else:
        print("Invalid Choice")
    continue_ch = input("Do you want to continue?(yes/no)")
    if continue_ch != "yes":
        print("Exiting the Temperature Conversion")
        break