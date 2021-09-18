# Importing classes
from dog import Dog
from owner import Owner

my_dog = Dog('chihuahua', 'Jeny', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("She is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
my_dog.is_vaccinated()
my_dog.owner = Owner('lily', 'smith', 'lily.s@gmail.com', '7629128392')
my_dog.owner.describe_owner()

your_dog = Dog('golden retriever', 'Louis', 8)
your_dog.describe_pet()
your_dog.sit()
your_dog.is_vaccinated()
your_dog.get_vaccination('canada clinic')
your_dog.is_vaccinated()

