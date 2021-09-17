# Moving items one list to another
# Register new customers into the regular customer list
new_customers = ['luis', 'alison', 'coby', 'suzy']

customers = ['lily', 'mary', 'john','david']
while new_customers:
    new_customer = new_customers.pop()

    print("Our new customer: " + new_customer.title())
    customers.append(new_customer)

print("\nCustomers :")
for customer in customers:
    print(customer.title())


# Removing all items of specific values
print("\nRemoving 'tiger' from a list")
animals = ['rabbit', 'monkey', 'panda', 'tiger', 'bear']
print(animals)

while 'tiger' in animals:
    animals.remove('tiger')

print(animals)
