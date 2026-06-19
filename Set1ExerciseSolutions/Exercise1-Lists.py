# creating a List of items (names of people)
namesOfPeople = ["Joshua", "Joan", "Jimmy", "Jin", "Julius"]

print(namesOfPeople)
# changing value of the first item
namesOfPeople[0] = "Janice"

print(namesOfPeople)
# adding an element to the list (sixth name)
namesOfPeople.append("Joseph")

print(namesOfPeople)
# adding an element at a specific position (3rd position)
namesOfPeople.insert(2, "Bathel")

print(namesOfPeople)
# Removing an Element from list (4th item)
namesOfPeople.pop(3)

print(namesOfPeople)
# printing last element of list using negative indexing
print(namesOfPeople[-1])

# created a new list and used range indexing to print 3rd,4th and 5th items
colors = ["Yellow", "Blue", "Orange", "Purple", "Red", "Green", "Indigo"]
print(colors[2:5])

# created a list of countries and made copy of it
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Ethiopia"]
countriesCopy = countries.copy()
print(countriesCopy)

# looping through list of countries
for country in countries:
    print(country)

# sorting a list of animals
animals = ["Dog", "Cat", "Cow", "Rat", "Snake", "Zebra", "Lion"]
# ascending sort
animalsAscend = sorted(animals)
print(animalsAscend)
# Descending sort
animalsDescend = sorted(animals, reverse=True)
print(animalsDescend)

# only print animals with letter a in them
for animal in animals:
    if "a" in animal:
        print(animal)

# joining two lists
#
firstName = ["Joshua"]
secondName = ["Ssentongo"]

name = firstName + secondName
print(name)
