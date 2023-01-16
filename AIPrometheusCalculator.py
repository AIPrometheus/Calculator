print("Addition = 1 Subtraction = 2 Multiplication = 3 Division = 4 Exponentiation = 5 Factorial = 6 Modulo = 7")

process=(input("Enter Process:"))

if process == '1':
    num1 = int(input("Enter Number:"))

    num2 = int(input("Enter Second Number:"))

    print("Result:",num1+num2)
elif process == '2':
    num1 = int(input("Enter Number:"))

    num2 = int(input("Enter Second Number:"))
    print("Result:",num1-num2)
elif process == '3':
    num1 = int(input("Enter Number:"))

    num2 = int(input("Enter Second Number:"))
    print("Result:",num1*num2)
elif process == '4':
    num1 = int(input("Enter Number:"))

    num2 = int(input("Enter Second Number:"))
    print("Result:",num1/num2)
elif process == '5':
    num1 = int(input("Enter Number:"))

    num2 = int(input("Enter Second Number:"))
    print("Result:",num1**num2)
elif process == '6':
    num1 = int(input("Enter Number:"))
    fact = 1

    for i in range(1, num1 + 1):
        fact = fact * i
    print("Result:",fact)
else:
    num1 = int(input("Enter Number:"))

    num2 = int(input("Enter Second Number:"))
    print("Result:", num1 % num2)
