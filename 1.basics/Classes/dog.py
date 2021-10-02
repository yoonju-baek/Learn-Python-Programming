from pet import Pet
from owner import Owner

# Creating a dog class - class keyword
# Dog class (child) inherits from Pet class (parent)
class Dog(Pet):
    """
    A simple attempt to model a dog.
    """

    # self parameter is required and must come first
    def __init__(self, type, name, age):
        """Initialize name and age attributes"""
        super().__init__(type, name, age)
        self.vaccination = False # Setting a default value
        self.owner = Owner() #Instance as attribute

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
    
    def is_vaccinated(self):
        """
        Print the dog is vaccinated or not
        """
        if self.vaccination:
            print(self.name.title() + " is vaccinated.")
        else:
            print(self.name.title() + " is not vaccinated.")

    def get_vaccination(self, location):
        self.vaccination = True
        print(self.name.title() + " has got a vaccination in the " + location.title() + ".")


