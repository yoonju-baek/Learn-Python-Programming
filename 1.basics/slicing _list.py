# Slicing a list
seasons = ['spring', 'summer', 'fall', 'winter']
# get specific group indice 0 through 2
print(seasons[0:2]) #elements 0, 1
print(seasons[2:3]) #element 2
print(seasons[:3]) #elements 0, 1, 2
print(seasons[1:]) #elements 1, 2, 3
print(seasons[-2:]) #prints the last two elements
print(seasons[:-2]) #prints the first two elements

# Looping through a slice
print('The first two seasons:')
for season in seasons[:2]:
    print(season)

# Copying a list
common_names = ['lily', 'james', 'john', 'jessica', 'adam', 'suzy']
friend_names = common_names[:]

print("my friend's names")
print(friend_names)

common_names.append('alex')
friend_names.append('olivia')

print('common names:')
print(common_names)
print("my friend's names")
print(friend_names)
