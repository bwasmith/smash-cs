# Pandas Cheatsheet
## Open/load
```python
import pandas as pd

data = pd.read_csv("CSY1Data.csv")

print(data.head())
```

## Series
### Simple Series Defintion (Creation)
```python
pies = pd.Series(["Pumpkin", "Pecan", 3.14, "Lemon Meringue", "Apple"])

print("pies[2] = " + str(pies[2]))

print(pies)
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

## Data Frames
```python
# Lists data types used in each columns
table.dtypes 

# Number of rows and columns 
table.shapes 

# Lists data types used in each column in the dataframe 
table.info() 

# Lists data types used in each column in the dataframe 
table.describe() 
round(table.describe(), 1)

# Accessing Rows
table.head(num)
table.tail(num)
table[a:b]
```

```python
# Select specific columns 
sleep_data = mammals[["mammal", "hours_of_sleep"]]

# Select rows based off of conditions
sleep_data[sleep_data["hours_of_sleep"] == 8]

# Set the index to be a specific column
mammals.set_index("mammal", inplace=True) 
mammals.reset_index(inplace=True)
```
