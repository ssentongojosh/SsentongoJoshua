def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("Welcome to The Menu Calculator")
print("How would you like to be served")
print("\n")

while True:
    print("1. addition (+)")
    print("2. subtraction (-)")
    print("3. multiplication (*)")
    print("4. division (/)")

    print("\n")
    option = input("Select your option : ")

    num1 = float(input("Enter the your first food value (a number) : "))
    num2 = float(input("Enter the your second food value (a number) : "))
    print("\n")
    match option:
        case "1":
            result = add(num1, num2)
            print(f"Here is your meal : {result}")
        case "2":
            result = sub(num1, num2)
            print(f"Here is your meal : {result}")
        case "3":
            result = mul(num1, num2)
            print(f"Here is your meal : {result}")
        case "4":
            result = div(num1, num2)
            print(f"Here is your meal : {result}")
        case "5":
            print("Sorry to see you go without a meal")
            break
        case _:
            print("Wrong selection option, try again (try 1,2,3 or 4)")
            continue
    print("\n")
    print("press c to continue or any key to quit")
    selection = input()
    match selection:
        case "c":
            continue
        case _:
            break
