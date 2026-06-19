# concatenating a string and int
num = 6
name = "Don"
nameNum = name + str(num)
print(nameNum)

# stripping space off a string
txt = "  Hello,     Uganda!    "
noSpace = txt.replace(" ", "")
print(noSpace)

# uppercase
upperCase = txt.upper()
print(upperCase)

# replace U with V
replaced = txt.replace("U", "V")
print(replaced)

# returning a range of characters in a string (2nd, 3rd, 4th)
y = "I am proudly Ugandan"
print(y[1:4])

# printing a string with nested double quotes
x = 'All "Data Scientists" are cool!'
print(x)
