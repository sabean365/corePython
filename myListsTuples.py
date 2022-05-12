#Code that explores the nature of lists and tuples in Python

#initialize list and tuple
my_list = [1,2,3]
my_tuple = (7,8,9)
my_list.append(4)
print(my_list)

# cannot append tuple
# my_tuple.append(4) <= does not work
# print(my_tuple)

print(my_tuple[2]) # element with value 9

#cannot change a tuple
# my_tuple[2] = 10 <= does not work

#a list is ordered and mutable and the is keyword checks if the object is the same
#two identical lists are two separate objects
print([1,2,3] is [1,2,3]) #false
#a tuple is ordered and immutable and is keywork checks the object
#because tuples are immutable, they point to the same place in memory and are the same object
print((1,2,3) is (1,2,3)) #true

#a list can contain multiple different variable types
my_list = ["hello", "universe", 42, 3.7, False, None, [1,2,3], {'x':1, 'y':3}]
print(my_list)

#Indexing behavior of a list -> remembering a list is mutable
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

#can copy a list
fruit_copy = fruits.copy() #returns a SHALLOW copy => not the same object
fruits.append("tomato")
print(fruits)
# fruits.clear() deletes everything in the list
print(fruit_copy)
print(fruits.count("apple"))
fruits.append(["blackberry", "kiwi"]) #creates a sublist within the list
print(fruits)
fruits.extend(['blackberry', "kiwi"]) #adds to the existing list
print(fruits)
fruit_copy.extend("tomato") #extends every character so that the characters in tomato become part of the list
print(fruit_copy)
fruits.insert(3,"raspberry") #inserts an element in the 4th place in the list
print(fruits)
fruits.pop() #pops last element from the list
print(fruits)
fruits.pop(11) #pops a specific index from the list
print(fruits)

#this removes every instance of the word apple from the list
fruits.remove("apple")
print(fruits)

#prints the list backwards
fruits.reverse()
print(fruits)

#sorts the list
fruits.sort() #default is alphabetical
print(fruits)

# while fruits:
  # print(fruits.pop()) #can pop them one by one

#tuples have a different behavior than lists
fruit = ("apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry")
#do not need parentheses for the tuple to be initialized
fruit2 = "apple", "apple", "blueberry", "cherry", "durian", "pineapple", "strawberry", "banana", "strawberry"
print(fruit[-1]) #prints the last element in the list
print(fruit[3]) #prints the fourth element in the list
print(fruit[1:5]) #prints 1-4 excluding 5
print(fruit[1:-1]) #prints from element 2 to 1 before the end
print(fruit[2:]) #prints all from element 3 onward
print(fruit[:-2]) #prints all elements except the last 2
print(fruit[1:-1:2]) #prints every other element from element 2 to the element before the last
print(fruit[1:8:2]) #prints every other element from element 2 to element 8
print(fruit[8:1:-1]) #prints elements backwards from 9 to 2 (not including 1)
print(fruit[::-1]) #prints elements backwards


print(type(fruits)) #list
print(type(fruit)) #tuple
print(type(fruit2)) #tuple

print(fruit.count("apple")) #counts how many instances of apple are in the tuple
print(fruit.index("blueberry")) #prints the index of blueberry in the tuple