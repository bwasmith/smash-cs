# Pandas Cheatsheet
## Open/load
```python
import pandas as pd

data = pd.read_csv("CSY1Data.csv")

# Get first 5 lines of data
output = data.head()

print(output)
```

## Series
### Simple Series Defintion (Creation)
```python
pies = pd.Series(["Pumpkin", "Pecan", 3.14, "Lemon Meringue", "Apple"])
print(pies)

# Access the second element and print. `str()` function is used to turn
# the number 3.14 to the string "3.14"
print("pies[2] = " + str(pies[2]))
```

### Series Definition (Creation) by w/ Index and Dictionary
```python
ingredients = pd.Series(["4 cups", "1 cup", "2 large", "1 cup"], index=["Flour", "Milk", "Eggs", "Sugar"])

print(ingredients)
print()

s = {"Los Angeles Dodgers": 2020, "New York Yankees": 2009,
    "Boston Red Sox": 2018, "Chicago Cubs": 2016, "San Francisco Giants": 2014,
    "Colorado Rockies": None}
world_series = pd.Series(s)

print(world_series)
```

### Mean Median Mode 1.7.6
```python
hot_dog_winners = pd.Series([72.0, 41.0, 70.0, 38.0, 62.0, 38.0, 61.0, 34.0, 69.0, 36.8],
              index=["Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Miki Sudo", 
              "Matthew Stonie", "Miki Sudo", "Joey Chestnut" ,"Miki Sudo",
              "Joey Chestnut", "Sonya Thomas"])

mean = hot_dog_winners.mean()
median = hot_dog_winners.median()
mode = hot_dog_winners.mode()
```

### Measures of Spread(Variance and Standard Deviation) 1.8.4
```python
people_named_anna = pd.Series([7288, 7118, 6846, 6808, 7523, 8564,
    8565, 8337, 8378, 9098, 10588, 10588,
    10385, 9443, 9514, 9101, 8601, 7888,
    7265, 6800, 6326, 5658, 5615, 5378,
    5679, 5125, 4775, 4520], index=["1990", "1991", "1992", "1993", "1994", "1995",
    "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005",
    "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015",
    "2016", "2017"])

variance = people_named_anna.var()
standard_deviation = people_named_anna.std()

# Find the range using the max and min values
max = people_named_anna.max()
min = people_named_anna.min()
range = max - min
```

### Get All Columns
```python
for c in data.columns:
    print(c)
```

### Plotting Data
```python
import pandas as pd
import matplotlib.pyplot as plt

people_named_anna = pd.Series([7288, 7118, 6846, 6808, 7523, 8564,
    8565, 8337, 8378, 9098, 10588, 10588,
    10385, 9443, 9514, 9101, 8601, 7888,
    7265, 6800, 6326, 5658, 5615, 5378,
    5679, 5125, 4775, 4520], index=["1990", "1991", "1992", "1993", "1994", "1995",
    "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005",
    "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015",
    "2016", "2017"])


print("People Named Anna")
print("--------------------")
print(people_named_anna)

# Plot a box plot
plt.hist(people_named_anna, edgecolor="black")
plt.show()
```

## DataFrames

### Creation from CSV File (Same as Above)
```python
import pandas as pd

data = pd.read_csv("CSY1Data.csv")

# Get first 5 lines of data
output = data.head()

print(output)
```


### Creation with Dictionary
```python
# data using a dictionary
data = {"mammal": ["African Elephant", "Bottlenose Dolphin", "Cheetah", "Domestic Cat", "Giraffe", "Ground Squirrel", "Horse", "House Mouse", "Human", "Killer Whale", "Lion", "Pig", "Rabbit"],
        "life_span": [70, 25, 14, 16, 25, 9, 25, 3, 80, 50, 15, 10, 5],
        "hours_of_sleep": [3, 5, 12, 12, 2, 15, 3, 12, 8, 3, 20, 8, 11],
        "speed": [40, 37, 110, 50, 50, 19, 69, 13, 45, 48, 80, 18, 56],
        "diet": ["plants", "meat", "meat", "meat", "plants", "both", "plants", "both", "both", "meat", "meat", "both", "plants"]
    }

# format data into a DataFrame
mammals = pd.DataFrame(data)

# print data to the console
print(mammals)

```

### DataFrame Info
```python
# Lists data types used in each columns
your_dataframe.dtypes

# Number of rows and columns
your_dataframe.shape

# Returns data types used in each column in the dataframe
your_dataframe.info()

# Returns data types used in each column in the dataframe
your_dataframe.describe()
# Round contents to nearest 1 decimal point
round(your_dataframe.describe(), 1)

# Accessing Rows
your_dataframe.head(num) #first `num` rows
your_dataframe.tail(num) #last `num` rows
your_dataframe[a:b] # rows a to b, not including b. [a:b)
```


### Selecting Columns 1.10.4
```python
data = {"mammal": ["African Elephant", "Bottlenose Dolphin", "Cheetah", "Domestic Cat", "Giraffe", "Ground Squirrel", "Horse", "House Mouse", "Human", "Killer Whale", "Lion", "Pig", "Rabbit"],
        "life_span": [70, 25, 14, 16, 25, 9, 25, 3, 80, 50, 15, 10, 5],
        "hours_of_sleep": [3, 5, 12, 12, 2, 15, 3, 12, 8, 3, 20, 8, 11],
        "speed": [40, 37, 110, 50, 50, 19, 69, 13, 45, 48, 80, 18, 56],
        "diet": ["plants", "meat", "meat", "meat", "plants", "both", "plants", "both", "both", "meat", "meat", "both", "plants"]
    }

# format data into a DataFrame
mammals = pd.DataFrame(data)

# Select ONE specific column
sleep_data_only = mammals["hours_of_sleep"]

# Select MULTIPLE specific columns
sleep_data = mammals[["mammal", "hours_of_sleep"]]

# Select columns from a condition
sleep_data[sleep_data["hours_of_sleep"] == 8]

# Select columns from multiple conditions
# In Pandas `|` means OR and `&` means AND
print(sleep_data[(sleep_data["hours_of_sleep"] == 8) |
                 (sleep_data["hours_of_sleep"] < 4)])

```

### Set Index 1.10.5
```python
# Set the index to be a specific column. This changes the DataFrame
mammals.set_index("mammal", inplace=True)
mammals.reset_index(inplace=True)
```

### Custom Scoring Function 1.11.2

Solution for 1.11.2
```python 
import pandas as pd

coasters = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None) # Displays all columns
print(coasters)


# create a function that uses the ranking algorithm
def ranking(speed, length, drop, duration):
    return (4 * speed) + (3 * length) + (5 * drop) + (4 * duration)

# use the function to create a new column with the calculations
coasters["ranking"] = ranking(coasters["Speed"], coasters["Length"], coasters["Drop"],coasters["Duration"])

# filter the table to display the name of the roller coaster and the
# ranking
filtered_table = coasters[["Coaster", "ranking"]]

# find the max value of the ranking column
max_value = coasters["ranking"].max()

# filter for the row that corresponds with the max value
row_with_max = filtered_table[coasters["ranking"] == max_value]

# print the answer!
print(row_with_max)
```

Second example for Custom Function
```python
import pandas as pd

data = {"student": ["Anayo", "Brandon", "Claudia", "Dave", "Evelyn", "Finn", "Gloria", "Hank", "Isla", "Julia"],
        "Test One": [84, 90, 50, 29, 49, 44, 30, 98, 31, 66],
        "Test Two": [68, 78, 28, 80, 45, 56, 53, 93, 31, 66],
        "Test Three": [42, 35, 30, 40, 28, 85, 80, 99, 38, 48]
    }

test_scores = pd.DataFrame(data)

# Custom function
# Input, Parameter: Three different test scores
# Return: Average of these scores
def average_score(test_one, test_two, test_three):
    return (test_one + test_two + test_three) / 3

# Create a new column "Average", and set it equal to the result of our custom function
test_scores["Average"] = average_score(test_scores["Test One"], 
                                test_scores["Test Two"], test_scores["Test Three"])

# Similar custom function, done in a different way
# Input, Parameter: a list of tests
# Return: the average of this list
def smarter_average_score(test_list):
    return sum(test_list) / len(test_list)

# Create a new column "Smarter Average", and set it equal to the result of our second custom function
# Note that we must pass a list to our smarter_average_score function as a parameter
test_scores["Smarter Average"] = smarter_average_score([test_scores["Test One"], 
                                test_scores["Test Two"], test_scores["Test Three"]])

print(test_scores)
```

### Counting Values

### Correlation
