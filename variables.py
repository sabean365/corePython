#String Operations
stringHello = "Hello World"
print(stringHello.replace("World", "Universe"))
print(r"Hello World")

#casting strings
x = float("10.2")
print(x)
y = complex("10.2")
print(y)

#ints and string literals
print(9 + 5)
print("9" + "5")

# append with +=
x = "Hello "
x += "World"
x

#the difference between == and is
x = ["Apple"]
y = ["Apple"]
print(x==y)
print(x is y)


#if statement can be one line
num = int(input("Enter an int: " ))
print("number is positive") if num > 0 else print

#ternary expression can execute a function and return a value
message = "number is even" if num % 2 == 0 else "Number is odd"
print(message)

#overloaded assignment variables
x = 5
y = "Hello Universe"

print(x)
print(y)

x = "This is a string now"
print(x)

name = ""

#String operations
first_string=f"Hello Universe, {name}!"
print(first_string, "Nikola")
print(first_string.capitalize())
print(first_string.lower())
print(first_string.upper())
print("There are " + str(first_string.count('l')) + " 'l's.")
print(first_string.find('ni'))
print(first_string.find('Ni'))
print(first_string.find('NI'))

#split function
print(first_string.split())
len(first_string)

#type function
print(type("Hello Universe"))
print(type(3.14))
print(type(12))

#isinstance function
print(isinstance(3, int))
print(isinstance("Nikola", str))
print(isinstance(3, str))

#casting
num=43.6
print(int(num))
print(str(num))
print(round(num))
print(float(num))