# Checking the condition of case is case sensitive
# Equality: ==
# Inequality: !=
# Mathematical comparisons: <, > <=, >=
# Multiple conditions: and, or

# Strings Comparisons
coffees = ['moca', 'espresso', 'americano', 'latte']

for coffee in coffees:
    if coffee == 'americano':
        print(coffee.title())
    else:
        print(coffee.upper())

# Numberical Comparisons
age = 17
if age == 25:
    print('Your age is 25')
else:
    print("Your age isn't 25")

# Checking multiple conditions
age = 25
gender = 'F'
if (age > 17) and (gender == 'F'):
    print('Female adult')
else:
    print('Not female adult')

# Checking condition in a list
teas = ['green', 'black', 'chai','lemon']
if 'chai' in teas:
    print('chai is in the list')
else:
    print('chai is not in the list')

# Or checking condition using 'not in'
if 'chai' not in teas:
    print('chai is not in the list')
else:
    print('chai is in the list')