num1 = 42   # variable declaration
num2 = 2.3  # variable declaration 
boolean = True  # Premitive
string = 'Hello World'  # Premitive
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # Dictionary
fruit = ('blueberry', 'strawberry', 'banana')   # Tuples
print(type(fruit))  # Log statement
print(pizza_toppings[1])    # Log statement
pizza_toppings.append('Mushrooms')  # List
print(person['name'])   # Log statement
person['name'] = 'George' # variable declaration
person['eye_color'] = 'blue'    # variable declaration
print(fruit[2])     # Log statement

if num1 > 45    # Conditional
    print("It's greater")   # Log statement
else:   # Conditional
    print("It's lower")     # Log statement

if len(string) < 5:     # Conditional
    print("It's a short word!")     # Log statement
elif len(string) > 15:  # Conditional
    print("It's a long word!")  # Log statement
else:   # Conditional
    print("Just right!")    # Log statement

for x in range(5):      # For loop
    print(x)    # Log statement
for x in range(2,5):    # For loop
    print(x)    # Log statement
for x in range(2,10,3):     # For loop
    print(x)    # Log statement
x = 0   # variable declaration
while(x < 5):   # While loop
    print(x)    # Log statement
    x += 1      # Variable declaration

pizza_toppings.pop()    # List
pizza_toppings.pop(1)   # List

print(person)   # Log statement
person.pop('eye_color')     # List
print(person)   # Log statement

for topping in pizza_toppings:  # For loop
    if topping == 'Pepperoni':  # Conditional
        continue    # For loop
    print('After 1st if statement')     # Log statement
    if topping == 'Olives':     # Conditional
        break       # For loop

def print_hello_ten_times():    # Function
    for num in range(10):   # For loop
        print('Hello')    # Log statement

print_hello_ten_times()     # Function

def print_hello_x_times(x):     # Function
    for num in range(x):    # For loop
        print('Hello')  # Log statement

print_hello_x_times(4)  # Function

def print_hello_x_or_ten_times(x = 10):   # Function
    for num in range(x):    # For loop
        print('Hello')  # Log statement

print_hello_x_or_ten_times()    # Function
print_hello_x_or_ten_times(4)   # Function


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