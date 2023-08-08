"""
Create a function that takes the age in years and returns the age in days.

Examples
calc_age(65) ➞ 23725

calc_age(0) ➞ 0

calc_age(20) ➞ 7300

"""

def calc_age(age):
    return age*365



print(calc_age(24)) #➞ 23725

print(calc_age(0)) #➞ 0

print(calc_age(20)) #➞ 7300


# Test.assert_equals(calc_age(10), 3650)
# Test.assert_equals(calc_age(0), 0)
# Test.assert_equals(calc_age(73), 26645)

# # Original challenge by @medyah99