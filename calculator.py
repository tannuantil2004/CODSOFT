def add (x,y):
    add = x+y
    print("this is the addition of given numbers :",add)
    return(x+y)


def subtract (x,y):
    subtract = x-y
    print("this is the subtraction of given numbers :",subtract)
    return(x-y)


def multiply (x,y):
    multiply = x*y
    print("this is the multiplication of given numbers :",multiply)
    return(x*y)


def divide (x,y):
    divide = x/y
    print("this is the division of given numbers :",divide)
    return(x/y)


def floor_divide (x,y):
    f_divide = x//y
    print("this is the floor division of given numbers :",f_divide)
    return(x//y)


def power (x,y):
    power = x**y
    print("this is the exponent of given numbers :",power)
    return(x**y)


def modulos (x,y):
    modulos = x%y
    print("this is the division reminder of given numbers :",modulos)
    return(x%y)



def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4/5/6/7): "))
            if choice in [1, 2, 3, 4,5,6,7]:
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("calculation in two formats")

    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 4:
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except:
            print("Division by 0 not possible!")
    elif choice == 5:
        print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
    elif choice == 6:
        print(f"{num1} ** {num2} = {power(num1, num2)}")
    elif choice == 7:
        print(f"{num1} % {num2} = {modulos(num1, num2)}")
       

def loop():
    choice = input("Do you want to continue? (Y,N): ")
    if choice.upper() == "Y":
        calculator()
    elif choice.upper() == "N":
        print("calculation ends here!")
    else:
        print("this is Invalid input!")
        loop()

if __name__ == "__main__":
    calculator()
    loop()
