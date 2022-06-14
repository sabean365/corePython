#Exercise to create an employee list

#create an empty list
emp_list = []

#create a while loop that will only break if integer is entered
while True:
  #use try to get the imput of an integer
  try:
    num_emp = int(input("How many employees are you going to enter? (Maximum is 10) "))
    #if the nunmber of employees is greater than 10, it will return to ask again
    if num_emp > 10:
      continue
  #Value error exception if it is not an integer
  except ValueError:
    print("You did not enter an integer.")
  #break out of the loop if you entered an integer
  else:
    break

#for loop to iterate through number of employees
for i in range(num_emp):
  employee = dict.fromkeys(["First Name", "Last Name", "Age"], None)
  first_name = input("Enter the employee's first name: ")
  last_name = input("Enter the employee's last name: ")

  while True:
    try:
      age = int(input("Enter the employee's age: "))
      if age < 18:
        raise Exception("Cannot have an employee under 18")
    except ValueError:
      print("You did not enter an integer.")
    except Exception as e:
      print(e)
      break
    #will only print and append if the employee is over 18
    else:
      employee["First Name"] = first_name.capitalize()
      employee["Last Name"] = last_name.capitalize()
      employee["Age"] = age
      print(f"Employee you entered is {employee}")
      emp_list.append(employee)
      break

#print the list
print(f"Your employee list is {emp_list}")