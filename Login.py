users = {
    "James":"password123",
    "John": "1234567890",
    "Julian": "loveBird123",
    "Jane":"helloworld"
}

roles = {
    "James":"Admin",
    "John": "Customer",
    "Julian": "Customer",
    "Jane": "cashier"
}


user = input("Enter Username : ")
password = input("Enter user password : ")

if user in users:
    if password == users[user]:
        match roles[user]:
            case "Admin":
                print("Logged in as Admin, full access granted")
            case "Customer":
                print("Logged in as Customer")
            case "Cashier":
                print("Logged in as Cashier")
            case _:
                print("")
    else:
        print("Incorrect password inserted, exiting")
else:
    print("Username doesnot exist, exiting")
