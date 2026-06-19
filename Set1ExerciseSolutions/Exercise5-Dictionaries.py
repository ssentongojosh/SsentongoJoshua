Shoes = {"brand": "Nick", "color": "black", "size": 40}

# updating value in a dictionary
Shoes["brand"] = "Adidas"

print(Shoes)

# Adding key value pair in a dictionary
Shoes["type"] = "sneakers"
print(Shoes)

# returning list of all keys in a dictionary
print(list(Shoes.keys()))

# returning list of values from a dictionary
print(list(Shoes.values()))

# checking if a key exists in a dictionary
if "size" in Shoes:
    print("Key size exist in the dictionary")

# looping through a dictionary
for key, value in Shoes.items():
    print(f"{key} : {value}")

# removing item from dictionary
Shoes.pop("color")
print(Shoes)

# emptying a dictionary
Shoes.clear()

print(Shoes)

# making a copy of a dictionary
Person = {"name": "James", "age": 40, "gender": "male"}

PersonCopy = Person.copy()

print(PersonCopy)

# nested dictionary
PersonNested = {
    "name": "James",
    "age": 40,
    "gender": "male",
    "address": {"Country": "Uganda", "City": "Kampala"},
}

print(PersonNested)
