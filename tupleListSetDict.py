my_list = [1,2,3]
my_tuple = (7,8,9)
my_list.append(4)
print(my_list)

# cannot append tuple
# my_tuple.append(4)
# print(my_tuple)

my_tuple[2]

#cannot change
# my_tuple[2] = 10

print([1,2,3] is [1,2,3]) #false
print((1,2,3) is (1,2,3)) #true

my_list = ["hello", "universe", 42, 3.7, False, None, [1,2,3], {'x':1, 'y':3}]
print(my_list)

fruits = ["apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry"]
fruits[3] = "mango"
print(fruits[-1])
print(fruits[3])
print(fruits[1:5]) #prints 1-4
print(fruits[1:-1]) 
print(fruits[2:])
print(fruits[:-2])
print(fruits[1:-1:2])
print(fruits[1:8:2])
print(fruits[8:1:-1])
print(fruits[::-1])

fruit_copy = fruits.copy() #returns a shallow copy
fruits.append("tomato")
print(fruits)
# fruits.clear() deletes everything
print(fruit_copy)
print(fruits.count("apple"))
fruits.append(["blackberry", "kiwi"]) #creates a sublist
print(fruits)
fruits.extend(['blackberry', "kiwi"]) #adds to the listg
print(fruits)
fruit_copy.extend("tomato") #extends every character
print(fruit_copy)
fruits.insert(3,"raspberry")
print(fruits)
fruits.pop() #pops last
print(fruits)
fruits.pop(11) #pops a specific index
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort() #default is alphabetical
print(fruits)

# while fruits:
  # print(fruits.pop()) #can pop them one by one

#tuples
fruit = ("apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry")
fruit2 = "apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry"
print(fruit[-1])
print(fruit[3])
print(fruit[1:5]) #prints 1-4
print(fruit[1:-1]) 
print(fruit[2:])
print(fruit[:-2])
print(fruit[1:-1:2])
print(fruit[1:8:2])
print(fruit[8:1:-1])
print(fruit[::-1])


print(type(fruits))
print(type(fruit))
print(type(fruit2))

print(fruit.count("apple"))
print(fruit.index("blueberry"))

##More Tuples
#examples of hou to declare
fruit = ("apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry")
fruit2 = "apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry"

#getting an element in the tuple
print(fruit[-1])
print(fruit[3])
print(fruit[1:5]) #prints 1-4
print(fruit[1:-1])
print(fruit[2:])
print(fruit[:-2])
print(fruit[1:-1:2])
print(fruit[1:8:2])
print(fruit[8:1:-1])
print(fruit[1])
print(fruit[::-1])



print(type(fruit))
print(type(fruit2))

print(fruit.count("apple"))
print(fruit.index("blueberry"))

x = [1,2,3]
y = ["a","b", "c"]
print("x + Y", x + y)
print(x + y) #concatenates
print("x*3" * 3)

[*x, *y] #behaves like the spread operator - will spread a list into a tuple

##Sets are mutable but not ordered.
my_set = {}
type(my_set)

fruit_set = {"apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry"}
print(type(fruit_set))
print(fruit_set)
fruit_set.add("tomato")
print(fruit_set)
fruit_set.update(("orange", "lemon"))
print(fruit_set)

spring_fruit = {"strawberry", "kiwi", "mango", "apricot", "kumquat", "pineapple", "lemon", "cherry", "grapefruit"}
print(spring_fruit.issubset(fruit_set))

print(fruit_set.intersection(spring_fruit))
all_fruits = fruit_set.union(spring_fruit)
print(all_fruits)


mixed_set = {1, 2, 3, "a", False, None, ("a","b","c")} #cannot add a list to a set but CAN have a TUPLE
print(mixed_set)

while all_fruits:
    print(all_fruits.pop()) #randomly removes elements in set

#Dictonary also curly brackets but are a key, value pair

user = {
    "username": "sarah",
    "password": "uni123",
    "friends":[456, 789],
    1: True,
    (1,2): [4,5]
}

#operations on dictionary
print(user["username"])
print(user["password"])
user["password"] = "uni8782"
user["username"] = "Daisy"
user["status"] = {"active": True, "banned": False}
user["friends"].append(1011)
print(user["status"]["active"])
print(user)
print(user.get("username"), user["username"]) #both methods return the same value

print(user.keys())
print(user.values())
print(user.items())
user.popitem()