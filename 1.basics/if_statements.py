# IF statements
# if, if-else, if-elif-else statements

age = 30

if age < 10:
    price = 4
elif age < 24:
    price = 10
elif age < 45:
    price = 20
else:
    price = 25

print('The cost is $' + str(price) + '.')

# If statements with lists
tea_toppings = ['tapioca', 'cream', 'blueberry pearl']

for tea_topping in tea_toppings:
    if tea_topping == 'cream':
        print('Adding cream will charge extra cost $2')
    else:
        print("Adding extra topping " + tea_topping + '.')

print('Finished ordering bubble tea')

# Checking a list is not empty
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print('Adding extra topping ' + topping)
else:
    print('no extra toppings')