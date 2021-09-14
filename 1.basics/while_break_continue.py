# Using break to exit a while loop
prompt = "Enter your favorite fruit: "
prompt += "\n(Enter 'quit' if you want to end the program.) "

while True:
    fruit = input(prompt)

    if fruit == 'quit':
        break
    else:
        print("My favorite fruit is an/a" + fruit + ".")

# Using continue in a while loop
# Find an odd numbers from 1 to 10
number = 0
while number < 10:
    number += 1

    if number % 2 == 0:
        continue 
    
    print(number)

