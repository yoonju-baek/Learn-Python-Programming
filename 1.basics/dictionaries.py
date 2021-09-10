# Dictionaries - a collection of key-value pairs {key:value}
fruit_0 = {'color': 'red', 'shape': 'circle'}
print(fruit_0)
print(fruit_0['color'])
print(fruit_0['shape'])

# Adding new key-value
fruit_0['price'] = 3
print(fruit_0)

# Modifying values
fruit_0['color'] = 'yellow'
fruit_0['shape'] = 'rectangle'
print(fruit_0)

# Removing key-value
del fruit_0['price']
print(fruit_0)

# Looping through a dictionary
print("Looping through a dictionary")
for key, value in fruit_0.items():
    print("\nKey: " + key)
    print("Value: "+ value)

# Looping through all the keys
# keys() method can be omit
family = {'father': 'david', 'mother': 'jessica', 'brother': 'john', 'sister': 'lily'}
print('Family members:')
for member in family.keys():
    print(member)

# Looping through all the values
print('Family names:')
for name in family.values():
    print(name.title())

# Only getting unique values
favorite_fruits = {'father': 'apple', 'mother': 'banana', 'brother': 'kiwi', 'sister':'apple'}
print('Fruits list:')
for fruit in set(favorite_fruits.values()):
    print(fruit.title())