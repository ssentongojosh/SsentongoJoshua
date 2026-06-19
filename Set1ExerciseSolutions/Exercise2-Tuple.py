x = ("samsung", "iphone", "tecno", "redmi")
# printing item from tuple x
print(x[0])

# using negative indexing to print 2nd item
print(x[-3])

# update iphone to itel
y = list(x)

y[1] = "itel"
x = tuple(y)
print(x)

# adding huawei to tuple
h = list(x)
h.append("huawei")
x = tuple(h)
print(x)

for phone in x:
    print(phone)

# remove first item from tuple
j = list(x)
j.pop(0)
x = tuple(j)

print(x)

# creating tuple using tuple constructor
cities = ["Kampala", "Jinja", "Arua", "Mbarara"]
cities = tuple(cities)
print(cities)

# unpacking a tuple
a, b, c, d = cities
print(a, b, c, d)

# using range indexes to print 2nd, 3rd and 4th cities
print(cities[1:4])

# joining tuples
firstName = ("Joshua",)
secondName = ("Ssentongo",)
name = firstName + secondName
print(name)

# multiplying a tuple
colors = ("Red", "Orange", "Yellow", "Blue")
print(colors * 3)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(f"8 appears {thistuple.count(8)} in thistuple")
