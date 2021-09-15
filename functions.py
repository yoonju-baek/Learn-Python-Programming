# Defining a function - the keyword "def"
def user_info(username, age):
    """Display user's information."""
    print("\nMy name is " + username.title() + ".")
    print("I am " + str(age) + " years old.")

user_info('lily', 30)

# Keyword arguments - the order doesn't matter
def describe_dog(name, type):
    """Describe information about a dog"""
    print("\nMy dog's name is " + name.title() + " and " + type + ".")

describe_dog(name='rooney', type='labrador retriever')
describe_dog(type='chihuahua', name='coco')

# Default values
def student_info(name, major, grade=3):
    print("\nThe major of " + name + " is " + major + " and " + name + " is in the " + str(grade) + " grade.")

student_info('john', 'computer science')