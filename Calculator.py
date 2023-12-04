def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Your y value cannot be 0")

def calculator():
    prev_result = None

    while True:
        print("This is a calculator")
        print("Please select an option")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("q. Quit")

        choice = input("Select an option (1/2/3/4/q): ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = input("Enter the first number or 'ans' : ")

            if num1 == 'ans' and prev_result is not None:
                num1 = prev_result
            else:
                num1 = float(num1)

            if choice != '4':
                num2 = input("Enter the second number or 'ans': ")
                if num2 == 'ans' and prev_result is not None:
                    num2 = prev_result
                else:
                    num2 = float(num2)
            else:
                num2 = input("Enter the divisor (second number) or 'ans': ")
                if num2 == 'ans' and prev_result is not None:
                    num2 = prev_result
                else:
                    num2 = float(num2)

            if choice == '1':
                prev_result = add(num1, num2)
            elif choice == '2':
                prev_result = sub(num1, num2)
            elif choice == '3':
                prev_result = multi(num1, num2)
            elif choice == '4':
                prev_result = divide(num1, num2)
            else:
                print("Invalid input")

            print(f"Result: {prev_result}")
        else:
            print("Invalid input")


calculator()