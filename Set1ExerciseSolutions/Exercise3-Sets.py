# creating a set of beverages
beverages = ["soda", "juice", "coffee"]
beverages = set(beverages)
print(beverages)

# adding items to a set

beverages.update(["energy drink", "milk"])
print(beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("microwave present in the set")

# removing item from set
mySet.discard("kettle")
print(mySet)

# looping through a set
for item in mySet:
    print(item)

# joining a list to a set
actors = {"Brad", "Robert", "Chris", "Holland"}
fruits = ["Mango", "watermelon"]

actorFruits = actors.union(fruits)

print(actorFruits)

# joining two sets
age = {30}
firstName = {"Joshua"}

agename = age.union(firstName)
print(agename)
