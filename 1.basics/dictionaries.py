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

# A list in a dictionary
bubble_tea = {
    'tea' : 'green',
    'sugar' : 'less',
    'ice' : 'normal',
    'toppings' : ['cheese cream', 'tapioca']
}

print("You ordered a " + bubble_tea['tea'] + " bubble tea with "+ bubble_tea['sugar'] + " sugar and " + bubble_tea['ice'] + " ice. The following toppings :")
for topping in bubble_tea['toppings']:
    print("\t" + topping)

# A dictionary in a dictionary
customers = {
    'john' : {
        'firstname' : 'john',
        'lastname' : 'smith',
        'phone' : '6472031234'
    },
    'jessica' : {
        'firstname' : 'jessica',
        'lastname' : 'lane',
        'phone' : '6478390274'
    }
}

for name, info in customers.items():
    print("The information of " + name)
    print("\tFull name: " + info['firstname'].title() + " " + info['lastname'].title())
    print('\tphone number: ' + info['phone'])