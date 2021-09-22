# try-except blocks
# handle zero division error
print("Enter two numbers to divide up")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        print(first_number + "/" + second_number + " = " + str(answer))