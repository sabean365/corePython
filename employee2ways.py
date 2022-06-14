#get name input
name = input("Enter employee's full name with one space between first and last name: ")

#split full name into two strings
name_split = name.split(" ")

#get age input
age = input("Enter the employee's age: ")

#parse age to int
age_int = int(age)

#import date
from datetime import date

#function to calculate birth year
today = date.today()
birth_year = today.year - age_int

#print name with proper capitalizaation
print("Employee name: " + name_split[0].title() + " " + name_split[1].title())

#print birth year
print("Employee's year of birth: " + str(birth_year))

#get last two digits of birth year
last_two = str(birth_year)[-2:]

#create email
print("Employee's email is: " + name_split[0].lower() + "." + name_split[1].lower() + last_two + "@company.com")

#Or do it another way using the input without having to cast variables...
#create first_name, last_name, full_name variables
first_name = name_split[0].title()
last_name = name_split[1].title()
full_name = first_name + " " + last_name

#create parts of email
first_lower = first_name.lower()
last_lower = last_name.lower()
dot = "."
email = "@company.com"

#using the format, print out the input
print("+++++++++++++++++++++++")
print("Using the Format Function")

print(f"Employee's name is: {full_name}")
print(f"Employee's year of birth: {birth_year}")
print(f"Employee's email is: {first_lower}{dot}{last_lower}{last_two}{email}")