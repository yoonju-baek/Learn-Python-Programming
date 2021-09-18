# Importing classes
from dog import Dog

my_dog = Dog('Jeny', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("She is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
my_dog.is_vaccinated()

your_dog = Dog('Louis', 8)
print("\nYour dog is " + your_dog.name + " and " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.is_vaccinated()
your_dog.get_vaccination('canada clinic')
your_dog.is_vaccinated()

