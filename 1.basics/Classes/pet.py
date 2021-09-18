class Pet():
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

    def describe_pet(self):
        print("\nI have a " + self.type)
        print("My pet's name is " + self.name.title() + " and " + str(self.age) + " years old.")