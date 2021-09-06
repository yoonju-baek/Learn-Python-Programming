# Defining a tuple = an immutable list
# A tuple can't be modified and deleted
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through a tuple
print('Print each value:')
for dimension in dimensions:
    print(dimension)

# Modifing a tuple => redefine the entire tuple
dimensions = (100, 250)
print('Modified demensons:')
print(dimensions)