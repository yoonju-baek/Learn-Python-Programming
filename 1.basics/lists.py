cars = ['Audi', 'BMW', 'Cadillac', 'Chevrolet', 'Mazda', 'Tesla']

print(cars)

# Access the individual items in a list
# first element
print('first element: ' + cars[0])

# last element
print(cars[5])
print('last element: '+ cars[-1])

# access second last element
print('second last element: '+ cars[-2])

# Modifying elements
cars[0] = 'Kia'
print('==After modifying first element==')
print(cars)

# Adding elements
# Appending elements to the end of a list
cars.append('Mercedes-Benz')
print('==After adding an element at the end==')
print(cars)

# Inserting elements at specific position into a list
cars.insert(1, 'Volvo')
print('==After inserting an element at the second position==')
print(cars)

# Removing elements from a list
# Using del statement
del cars[0]
print('==After removing an first element==')
print(cars)

# Using pop() method - return the last item after removing it from a list
popped_car = cars.pop()
print('The last element: '+ popped_car)
print(cars)

# Poping elements from a specific position in a list
popped_fifth_car = cars.pop(4)
print('fifth element: '+ popped_fifth_car)
print(cars)

# Removing an item by value
# remove() method
cars.remove('BMW')
print('==After removing BMW from the list==')
print(cars)


# Organizing a list
# Ascending sorting a list permanently and alphabetically - sort() method
cars.sort()
print(cars)

# Descending sorting a list permanently and alphabetically - sort() method
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily - sorted() function
print('==Temporarily sorting==')
print(sorted(cars))
print(sorted(cars, reverse=True))

# Printing a list in reverse order
new_cars = ['Toyota', 'Genesis', 'Tsuru', 'Camry']
print('==New Cars==')
print(new_cars)

print('==Reverseing order==')
new_cars.reverse()
print(new_cars)

# Finding the length of a list - len() function
print('The length of the list of new cars: '+ str(len(new_cars)))





