# Python Cheat Sheet
## Vocabulary

**Boolean** - Data type for True or False values  
**Comments** - Using a ‘#’  so Python will ignore anything afterward  
**Computer programs** - How a computer does everything it does  
**Dictionary** - Data structure for holding key-value pairs  
**Float** - Data type for numbers with decimal point  
**Function** - A piece of code which can take inputs(parameters) and can return a value  
**Integer** - Data type for numbers with no decimal point  
**Library** - A collection of code that others have written that we can access and use  
**List** - Data structure for holding several variables  
**Loop** - A method for going one-by-one over each item in a data structure  
**Open Source** - How the program is written is is available publicly. (E.g. Chrome is not fully open source, Firefox is)  
**Pandas** - A data science library we will use  
**Parameter** - Inputs into a function
**Programming** - Coding, writing of computer programs  
**Python** - The programming language we will be using for this course  
**String** - Data type for words and letters  
**Variable** - Named unit of data that is assigned a value  

## Print
```python
print("Hello World")
```

## Variables
```python
x = 10
print(x)
```

```python
some_integer = 10 # Integer

some_float = 3.14 # Float

some_boolean = True # Boolean

some_string = "Brendan" # String
```

## Math
```python
sum = 20 + 50
print(sum)

# Mathematical operators in Python:
# + Addition
# - Subtraction
# * Multiplication
# / Division
# ** Exponentiation
# % Modulo (remainder)
```

## Comparisons
```python
# == Equals
# != Not Equals
# < Less than
# <= Less than or equal to
# > Greater than
# >= Greater than or equal to

lies = 10 == 5
print(lies)
truth = 10 != 5
print(truth)
```

## Conditionals (`if` statements)
```python
hungry = True
if hungry:
    print("I am hungry")
else:
    print("I am not hungry")
```

## Indentation
```python
hungry = False
if hungry:
    print("I am hungry")
print("I print regardless of hunger")
```

_End day 4_

## Conditionals Cont. (`else`, `elif`)
```python
# if, else
num = 5
if num % 2 == 0:
    print("This is even")
else:
    print("This is odd")

# elif
num = 5
if num % 2 == 0:
    print("This is even")
elif num % 3 == 0:
    print("This number is odd and divisible by 3")
```

## Compound Conditionals (`and`, `or`)
```python
num = 50
if num > 0 and num % 2 == 0:
    print("This number is a positive even number")

if num < 0 or num > 100:
    print("This number is either less than 0 or greater than 100")
```

## Loops (`for`)
```python
for x in range(1, 100):
    print(x)
```

## Lists
```python
some_food = ["apples", "oranges", "mangoes"]

# Print all items in the list
for food in some_food:
    print(food)

# Access one item in the list
print(some_food[0])

# Change the value of an item in the list
some_food[0] = "pasta"
print(some_food[0])
```

## Dictionaries
```python
our_dictionary = {
    "element1": "value for element1",
    "element2": "value for element2"
}

# Access an element in a dictionary
print(our_dictionary["element1"])

# Change an element in a dictionary
our_dictionary["element1"] = "new value"

# Add new elements to a dictionary
our_dictionary["new element"] = "new element's value"

# Print the entire dictionary
print(our_dictionary)
```

## Functions
```python
# DEFINE a function
def silly_function():
    return 10

# CALL a function
x = silly_function()
print(x)

# Parameters a, b
def sum(a, b):
    return a + b

print(sum(1, 2))
```

## Imports

```python
import random
random_integer = random.randint(1, 10)
```
