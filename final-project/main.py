import pandas as pd

# Read dataset
data = pd.read_csv("CSY1Data.csv")

# Get the Calculus AB test scores from dataset
calculus_scores = data.loc[2]

# Prepare variables for the sums I need
males_passing_sum = 0
females_passing_sum = 0
another_passing_sum = 0
males_failing_sum = 0
females_failing_sum = 0
another_failing_sum = 0

# *index* is the column race, gender, score. Such as: AMERICAN INDIAN/ALASKA NATIVE MALES 5
# *value* is the number of tests with that race, gender, score
#for each race, gender, score combination
for index, value in calculus_scores.items():
    # if the column is female
    if "FEMALES" in index:
        # if the column is a passing test
        if "5" in index or "4" in index or "3" in index:
            #add to the female passing sum
            females_passing_sum += value
        else:
            # add to the female failing sum
            females_failing_sum += value
    elif "MALES" in index:
        if "5" in index or "4" in index or "3" in index:
            males_passing_sum += value
        else:
            males_failing_sum += value
    elif "ANOTHER" in index:
        if "5" in index or "4" in index or "3" in index:
            another_passing_sum += value
        else:
            another_failing_sum += value

print("For the AP Calculus AB Test")
print("___________________________")
print("Pass/Fail Totals:")
print("Total Males Passing: ", str(males_passing_sum))
print("Total Males Failing: ", str(males_failing_sum))
print("Total Females Passing: ", str(females_passing_sum))
print("Total Females Failing: ", str(females_failing_sum))
print("Total Anothers Passing: ", str(another_passing_sum))
print("Total Anothers Failing: ", str(another_failing_sum))

# Calculate pass rate for each gender
male_pass_rate = males_passing_sum / (males_passing_sum + males_failing_sum)
female_pass_rate = females_passing_sum / (females_passing_sum + females_failing_sum)
another_pass_rate = another_passing_sum / (another_passing_sum + another_failing_sum)

# Round to make it more readable
male_pass_rate = round(male_pass_rate, 4)
female_pass_rate = round(female_pass_rate, 4)
another_pass_rate = round(another_pass_rate, 4)

print()
print("Pass Rates:")
print("Male Pass Rate: ", str(male_pass_rate))
print("Female Pass Rate: ", str(female_pass_rate))
print("Another Pass Rate: ", str(another_pass_rate))
