print("=============Welcome to the contact manager system===========")
contacts = [
    {"name": "James", "phone": "0712345678", "email": "james@gmail.com"},
    {"name": "John", "phone": "0798765432", "email": "john@gmail.com"},
]


def validate_name():
    while True:
        name = input("Enter name: ")
        if len(name) > 20:
            print("Name too long (Maxium 20 characters)")
            continue
        else:
            name = name.title()
            return name


def validate_phone():
    while True:
        phone = input("Enter phone number (like 07xxx): ")
        if len(phone) != 10:
            print("phone number too long/short, enter a valid number please! ")
            continue
        elif not phone.isdigit():
            print("Phone number should not contain characters, try again ")
            continue
        elif phone[0:2] != "07":
            print("Phone number should start with 07, Try again")
            continue
        else:
            return phone


def validate_email():
    while True:
        email = input("Enter the email: (e.g yourname@gmail.com): ")
        if "@" and "." not in email:
            print('invalid email, should contain "@" and "." ')
            continue
        elif (
            email.index("@") > email.index(".")
            or email.index("@") + 1 == email.index(".")
            or email.index("@") == 0
            or email.index(".") == len(email) - 1
        ):
            print("invalid email, try again")
            continue
        else:
            return email


def add_contact():
    name = validate_name()
    phone = validate_phone()
    email = validate_email()
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully")


def view_contact():
    query = input("Enter name or email : ")
    for contact in contacts:
        if contact["name"] == query.title() or contact["email"] == query.title():
            print("========Contact information=========")
            print(f"name: {contact['name']}")
            print(f"Phone number : {contact['phone']}")
            print(f"email: {contact['email']}")
            break
    else:
        print("No matching contact information found, try again ")


def update_contact():
    name = ""
    email = ""
    phone = ""
    query = input("Enter the name, email or phone number to update : ")
    for contact in contacts:
        if (
            contact["name"] == query.title()
            or contact["email"] == query.title()
            or contact["phone"] == query
        ):
            name1 = contact["name"]
            phone1 = contact["phone"]
            email1 = contact["email"]
            print("============current contact info================")
            print(f"name: {contact['name']}")
            print(f"Phone number : {contact['phone']}")
            print(f"email: {contact['email']}")

            while True:
                selection = input("Would you like to change the name? Y/N : ")
                selection = selection.lower()
                if selection not in ["y", "n"]:
                    print("Invalid option, try again")
                    continue
                elif selection == "y":
                    name = validate_name()
                    break
                else:
                    name = name1
                    break
            while True:
                selection1 = input(
                    "Would you like to change the phone number? Y/N: "
                ).lower()
                if selection1 not in ["y", "n"]:
                    print("Invalid option, try again")
                    continue
                elif selection1 == "y":
                    phone = validate_phone()
                    break
                else:
                    phone = phone1
                    break

            while True:
                selection = input("Would you like to change the email? Y/N: ").lower()
                if selection not in ["y", "n"]:
                    print("Invalid option, try again")
                    continue
                elif selection == "y":
                    email = validate_email()
                    break
                else:
                    email = email1
                    break

            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email
            print("Contact updated successfully. ")
            break
    else:
        print("No matching contact information found, try again ")


def delete_contact():
    query = input("Enter the name, email or phone number to delete:")
    flag = True
    for contact in contacts:
        if (
            contact["name"] == query
            or contact["email"] == query
            or contact["phone"] == query
        ):
            contacts.pop(contacts.index(contact))
            print("contact deleted successully")
            flag = False
    if flag:
        print("contact not found")


def search_contact():
    query = input("Enter the name, email or phone number to search : ")
    flag = True
    print("=============== Search results ===================")
    for contact in contacts:
        if (
            query in contact["name"]
            or query in contact["email"]
            or query in contact["phone"] == query
        ):
            print(f"name: {contact['name']}")
            print(f"Phone number : {contact['phone']}")
            print(f"email: {contact['email']}")
            print("\n")
            flag = False
    if flag:
        print("No contact found from search")


def all_contacts():
    print("=========== contact list =============")
    for contact in contacts:
        print(f"name: {contact['name']}")
        print(f"Phone number : {contact['phone']}")
        print(f"email: {contact['email']}")
        print("\n")


while True:
    print(
        """
    === Contact Manager Menu ===
    1. Add Contact
    2. View Contact
    3. Update Contact
    4. Delete Contact
    5. Search Contacts
    6. List All Contacts
    7. Exit
    """
    )
    choice = input("Choose an option (1-7): ")
    print("")
    match choice:
        case "1":
            add_contact()
        case "2":
            view_contact()
        case "3":
            update_contact()
        case "4":
            delete_contact()
        case "5":
            search_contact()
        case "6":
            all_contacts()
        case "7":
            break
        case _:
            print("Invalid selection, try again")
            continue
