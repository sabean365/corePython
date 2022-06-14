##FizzBuzz program

#get user input
num = (input("Please enter an integer between 10 and 100: "))

#create a list
list_fb = [0]

#make range from 1
rnum = range(1, int(num))

#integers, fizzes, buzzes and fizzbuzzes initialized
i1 = 0
f = 0
b = 0
fb = 0

#create for loop
for i in rnum:
    #if is divisible by 3 & 5
    if i % 3 == 0 and i % 5 == 0:
        list_fb.append("FizzBuzz")
        fb +=1
    elif i % 3 == 0:
        list_fb.append("Fizz")
        f +=1
    #if is divisible by 5
    elif i % 5 == 0:
        list_fb.append("Buzz")
        b +=1
    #if none of the above
    else:
        list_fb.append(i)
        i1 +=1

from pprint import pprint
pprint(list_fb)

total = 0

for j in list_fb:
  if isinstance(j, int): total += 1

#totals using lists {}
print(f"The total of integers is {total}")
print(f"The count of Fizz is {list_fb.count('Fizz')}")
print(f"The count of Buzz is {list_fb.count('Buzz')}")
print(f"The count of FizzBuzz is {list_fb.count('FizzBuzz')}")

#totals using counters
print("There were " + str(fb) + " fizzbuzzes.")
print("There were " + str(f) + " fizzes.")
print("There were " + str(b) + " buzzes.")
print("There were " + str(i1) + " integers.")