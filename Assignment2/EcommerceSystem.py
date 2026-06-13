# SSentongo Joshua 2400701345 24/U/1345
# Ecommerce System with login, signup, product selection, coupon insertion and calculates Discount
users = {
    "James": "password123",
    "John": "1234567890",
    "Julian": "loveBird123",
    "Jane": "helloworld",
}

roles = {"James": "Admin", "John": "Customer", "Julian": "Customer", "Jane": "cashier"}


def calculateFinalPrice():
    # SSentongo Joshua 2400701345 24/U/1345

    tax_rate = 0
    coupon = None
    discount = 0
    coupon_codes = ["ABC123", "DEF456", "GHI789"]
    locations = ["Kampala", "jinja", "Mbarara"]
    subtotal = 14000

    products = {"Tv": 20000, "Radio": 30000, "Fridge": 45000}
    print("...................Available Products.................")

    for item in products:
        print(f"{item} : {products[item]}")
    print("")

    while True:
        product = input("Type Product name : ")
        product = product.title()
        if product in products:
            subtotal = products[product]
            print(f"subtotal : {subtotal}")
            break
        else:
            print("invalid Selection, Try Again")

    coupon = input("Enter coupon code if any else press enter : ")

    if coupon:
        if coupon in coupon_codes:
            print("Valid Coupon")
            discount = 10
            print(f"Coupon discount applied : {discount}%")
        else:
            print("Invalid coupon")
    else:
        print("No coupon entered")
    print("")

    print("Available locations")
    for city in locations:
        x = locations.index(city) + 1
        print(f"{x}.{city}")
    print("")

    y = True
    while y:
        choice = input("Select in your location : ")
        match choice:
            case "1":
                tax_rate = 5
                y = False
            case "2":
                tax_rate = 3
                y = False
            case "3":
                tax_rate = 7
                y = False

            case _:
                print("invalid input")

    match subtotal:
        case n if 10000 <= n <= 20000:
            discount += 7
            print(f"discount applied on subtotal: {discount}%")
        case n if 20001 <= n < 30000:
            discount += 10
            print(f"discount applied on subtotal : {discount}%")
        case n if 30001 <= n < 45000:
            discount += 12
            print(f"discount applied on subtotal : {discount}%")
        case _:
            print("")

    discountAmount = subtotal * (discount / 100)
    print(f"Discount Amount : {int(discountAmount)}")
    taxAmount = subtotal * (tax_rate / 100)
    print(f"Tax Amount : {int(taxAmount)}")
    finalPrice = subtotal + taxAmount - discountAmount
    print(f"final price is : {finalPrice}")


print(""" #######################################
Welcome to the Spark E-commerce commandline System
Please select Login or SignUp below
##################################################
    """)

print("1. Login")
print("2. SignUp")


def login():
    print("######   Login   ########")
    user = input("Enter Username : ")
    password = input("Enter user password : ")

    if user in users:
        if password == users[user]:
            match roles[user]:
                case "Admin":
                    print("Logged in as Admin, full access granted")
                case "Customer":
                    print("")
                    print("######    Logged in as Customer     ######")
                    print("")
                    calculateFinalPrice()
                case "Cashier":
                    print("Logged in as Cashier")
                case _:
                    print("")
        else:
            print("Incorrect password inserted, exiting")
    else:
        print("Username doesnot exist, exiting")


def signup():
    print("###### SignUp  #########")
    print("Note : you are signing up as a Customer")
    print("")
    username = input("Enter username : ")
    password = input("Enter password : ")
    users[username] = password
    roles[username] = "Customer"

    print("")
    print("Now proceed to login........")
    print("")
    login()


x = True
while x:
    choice = input("Select a Choice (1 or 2) : ")
    match choice:
        case "1":
            login()
            x = False
        case "2":
            signup()
            x = False
        case _:
            print("invalid choice, try again")
