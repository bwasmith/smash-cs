# Python Cheat Sheet
## Vocabulary

*Boolean* - Data type for True or False values  
*Comments* - Using a ‘#’  so Python will ignore anything afterward  
*Computer programs* - How a computer does everything it does  
*Float* - Data type for numbers with decimal point  
*Integer* - Data type for numbers with no decimal point  
*Library* - A collection of code that others have written that we can access and use  
*Open Source* - How the program is written is is available publicly. (E.g. Chrome is not fully open source, Firefox is)  
*Pandas* - A data science library we will use  
*Programming* - Coding, writing of computer programs  
*Python* - The programming language we will be using for this course  
*String* - Data type for words and letters  
*Variable* - Named unit of data that is assigned a value  

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

## Conditionals (“if” statements)
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
