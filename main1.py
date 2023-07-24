
DATA TYPES

name = "Beau" String
print (type(name) == str) Type of name is a string hence why it is TRUE

print (isinstance(name,str))

The isinstance() function returns True if the specified object is of the specified type, otherwise False .

age = 2
print (isinstance(age,float )) -  not a float because it doesn't have a decimal

python automatically detects the type from the value type

number = "20"
age = int(number)
print (isinstance(age,int)) 
This is called CASTING - trying to extract int from this string.


DIFFERENT TYPES OF TYPES 

complex for complex numbers
bool for booleans
list for lists
tuple for tuples 
range for ranges
dict for dictionaries
set for sets 

age = int (number)

=  assignment operator
+,-,%,* arithmetic operator
>,< relational operator

a = 1
b = 2

a == b false
a != b true
a > b false
a <= b true

Boolean Operators

condition1 = True
condition2 = False

not condition1 - False
condition1 and condition2 - False
condition1 or condition2 - True

OR
print(0 or 1) - 1
 (False or 'hey') - 'hey'
print('hi' or 'hey') - 'hi'
print([] or False) - False
print(False or []) - '[]'

AND
print(0 and 1) - 0
print(1 and 0) - 0
print(False and 'hey') - False
print('hi' and 'hey') - 'hey'
print([] and False) - []
print(False and []) - False

BITWISE OPERATORS

& performs binary AND 
| performs binary OR 
^ performs a binary XOR operation
~ performs a binary NOT operation
<< shift left operation
>> shift right operation

TERNARY OPERATOR 

def is_adult(age):
    if age > 18:
      return True
      else:
           return False

def is_adult2(age):
    return True if age > 18 else False

STRINGS

print("beau".upper())

print("bEAu".lower())

print("bEAu person".title())

print("bEAu person".islower()) - False

print("person".islower()) - True

insert imgs you took of string methods

name = "Beau"
print(name.lower())
print(name)     

name = "Beau"
print(name.lower())
print(len(name)) - len means length     

name = "Beau"
print(name.lower())
print("au" in name) - True as there is a au in Beau

STRING CHARACTERS & SLICING

name = 'Be\\au'
print(name)

name = 'Beau'
print(name[1]) - shows 'e' which is the 2nd letter

name = 'Beau is cool'
print(name[5:7]) 

BOOLEANS

done = True

if done:
  print("yes")
else:
  print("no") - yes 

done = False

if done:
  print("yes")
else:
  print("no") - no

done = 0 - no , 10 - yes , -1 - yes , "" - no

if done:
  print("yes")
else:
  print("no")

done = True

print(type(done) == bool)

if done:
  print("yes")
else:
  print("no")

ans - True , yes

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])

NUMBER DATA TYPES

num1 = 2 + 3j
num2 = complex(2,3)

print(num2.real,num2.imag)
ans- 2.0.3.0

print(abs(-5.5))
ans - 5.5

print(round(5.5))
ans - 6 

ENUMS

from enum import Enum

class State(Enum):
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE.value) - 1
print(State(1)) - State.ACTIVE

USER INPUT

age = input("What is your age ? ")
print("Your age is " + age)

CONTROL STATEMENTS

condition = False

if condition == True:
   print("The condition")
   print("was true")

else:
  print("The condition")
  print("was false")

LIST

dogs = ["Roger",1, "Syd", True]

print("Roger" in dogs) - True
print("Beau" in dogs) - False

dogs = ["Roger",1, "Syd", True,"Quincy",7]

dogs.append("Judah") - adds Judah
dogs.extend(["Judah", 5]) - adds Judah & 5
dogs+= ["Judah",5]
dogs += "Judah" - adds each letter
dogs.remove("Quincy") - removes names


print(dogs.pop())
print(dogs)

items = ["Roger",1, "Syd", True,"Quincy",7]

items.insert(2, "Test") - inserts Test at the "third" item as it is 0,1,2,etc 

items[1:1] = ["Test1", "Test2"]

print(items)
 
SORTING LISTS

items = ["Roger", "bob", "Beau","Quincy"]
itemscopy = items[:]
items.sort(key=str.lower)

print(sorted(items, key=str.lower))

print(items)
print(itemscopy)

TUPLES

names = ("Roger", "Syd", "Beau")

names[-1]
names.index("Roger")

len(names)

print("Roger" in names)
print(sorted(names))
newTuple = names + ("Tina", "Quincy")

DICTIONARIES

dog = { "name": "Roger", "age": 8, "color": "green"}

dog["name"] = "Syd"
print(dog.get("color", "brown"))
print(dog.pop(""))



