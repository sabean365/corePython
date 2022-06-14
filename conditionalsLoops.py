#conditionals

#get x
x=int(input("Please enter number #1 to compare: "))
#get y
y=int(input("Please enter number #2 to compare: "))

if x>y:
  if x % 2 == 0:
    print("X is larger than y and is even.")
  else:
    print("Y is larger than s and is odd.")
elif y>x:
    if y % 2 == 0:
      print("Y is larger than x and is even.")
    else:
      print("Y is larger than x and is odd.")

##For loops
smoothie = {"strawberry", "kiwi", "pineapple", "lemon", "cherry", "blackberry"}

smoothie_iterator = iter(smoothie)
print(smoothie)

print(next(smoothie_iterator))
print(next(smoothie_iterator))

r10 =  range(10)
print(r10)
print(r10[-1])

#A for loop will operate over any sequence (iterable object)
for fruits in smoothie:
  print(fruits[0])

#vertical output
#using range + count by
for i in range(10, 1, -2):
  print(i)

for i in range(1, 10, 1):
  print(1)

#vertical printing
l1 = [1,2,3]
l2 = ["a", "b", "c"]

#using len/printing columns
for i in range(len(l1)):
  print(l1[i], l2[i])