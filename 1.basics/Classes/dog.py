# Creating a dog class - class keyword
class Dog():
    """
    A simple attempt to model a dog.
    """

    # self parameter is required and must come first
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        self.vaccination = False # Setting a default value

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


