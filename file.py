num1 = 42
#- variable declaration,Data Types: Primitive, Numbers
num2 = 2.3
# variable declaration, Data Types: Primitive, float numbers
boolean = True
# variable declaration, Data Types, Primitive Boolean  
string = 'Hello World'
#Variable declaration, Data Types: Primitive, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#Variable declaration, Data Types, Composite, List: Array of Strings., Initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#Variable declaration, Data Type, Composite, Dictionary, Initialize
fruit = ('blueberry', 'strawberry', 'banana')
#Variable declaration, Data Type, Composite, Truples,  Initialize
print(type(fruit))
#log statement, (type check, variable, Composite: Truple, Access value)
print(pizza_toppings[1])
#log statement, (variable declaration, Composite: List, Access Value of index 1, in list)
pizza_toppings.append('Mushrooms')
#variable declaration, Composite: list, add value(mushrooms) to end of list
print(person['name'])
#log statement, function parameter, Data Type: Tuples
person['name'] = 'George'
# access value of list, and changing the value from John to George.
person['eye_color'] = 'blue'
#access value of list, and changing the value - 
# - NameError: name <variable name> is not defined
print(fruit[2])
#log statement. Data Type: Truple,Access Value

if num1 > 45:
    print("It's greater")
#if value of num1 is greater than 45
#print "It's greater"
else:
    print("It's lower")
#else log statement, It's lower
if len(string) < 5:
#if length check is less than 5
    print("It's a short word!")
#log statement(It's a short word!)
elif len(string) > 15:
#else if length check 
    print("It's a long word!")
#if elif statment statement is true, log statement "It's a long word"
else:
    print("Just right!")
#if elif statement is false, log statement "Just right"
for x in range(5):
#for loop x to loop from 0 to 4
    print(x)
#log each each time x iterates through the for loop
for x in range(2,5):
# for loop x to iterate starting at 2 to 5
    print(x)
# log statement for each time iterates from 2 to 5
for x in range(2,10,3):
#for x in range from the number 2 to 10 in increments of 3
    print(x)
#print the value of x every time it iterates through range
x = 0
#we a declaring the variable x equals 0
while(x < 5):
#while x is less than 5
    print(x)
#print each time x iterates through the while loop
    x += 1
#variable x += 1


pizza_toppings.pop()
#declaring that we are taking the first variable and removing it from the pizza_toppings list of strings
pizza_toppings.pop(1)
#declaring that we are taking the variable in the postition of index 1 and removing it from the pizza_toppings list of strings

print(person)
#log statement : print the value in the variable person
person.pop('eye_color')
#variable declaration, removing the value 'eye color' from the variable person list
print(person)
#log statement, print the value(s) inside the variable person


for topping in pizza_toppings:
#for loop using a toppings as a variable to iterate through pizza_toppings
    if topping == 'Pepperoni':
#if toppng is equal to the value 'pepperoni
        continue
        #continue
    print('After 1st if statement')
#print 'After 1st if statement'
    if topping == 'Olives':
#if toppings is equal to the value 'Olives'
        break
#break

def print_hello_ten_times():
#function called print_hello_ten_times
    for num in range(10):
#for loop, variable num will loop starting at zero to 9
        print('Hello')
#print 'hello'

print_hello_ten_times()
#calling the function
def print_hello_x_times(x):
creating function called "print hello x times"
    for num in range(x):
#for loop, variable num used to iterate through the values of x
        print('Hello')
#print Hello however many times it iterates through x

print_hello_x_times(4)
# print function "hello x times 4 times" because 4 is being passed through the variable x as an argument
def print_hello_x_or_ten_times(x = 10):
# created a function print_hello_x_or_ten_times
#x is used as an argument in the paranthesis

    for num in range(x):
#for loop, variable is used as a variable to iterate through the values of x
        print('Hello')
#prints hello every time num iterates through x
print_hello_x_or_ten_times()
#called function hello_x_or_ten_times
print_hello_x_or_ten_times(4)
# calling function and passing the argument of 4 through x

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)