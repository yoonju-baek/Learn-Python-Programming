class Owner():
    """Owner's information"""
    def __init__(self, first_name='', last_name='', email='', phone=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def describe_owner(self):
        print("The name of owner is " + self.first_name + " " + self.last_name + ".")
