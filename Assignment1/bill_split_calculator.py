# BY SSENTONGO JOSHUA 2400701345


print("Welcome to the Billl split Calculator")


billAmount = float(input("Enter Total Bill Amount : "))
numberOfPeople = int(input("Enter Number of People : "))
tipPercentage = float(input("Enter tip percentage (between 1 and 100) : "))

tipAmount = (tipPercentage/100)*billAmount
totalBill = billAmount + tipAmount
amountPerPerson = totalBill/numberOfPeople

print("_______________________________________________________")
print("                        RECEIPT")
print("_______________________________________________________")
print(f"    # Bill Amount         :   {billAmount}  ")
print(f"    # Number of People    :   {numberOfPeople}  ")
print(f"    # Tip Percentage      :   {tipPercentage}  ")
print(f"    # Tip Amount          :   {tipAmount}  ")
print(f"    # Total Bill Amount   :   {totalBill}  ")
print(f"    # Amount Per Person   :   {amountPerPerson}  ")

print("_______________________________________________________")
print("\n")
