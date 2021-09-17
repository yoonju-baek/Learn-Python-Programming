# Manupulate an arbitrary number of arguments
def make_bubble_tea(tea, *requests):
    """
    Print the list of toppings that have been requested.
    """
    print("\nYour own bubble tea: " + tea.title())
    for request in requests:
        print(request)

#make_bubble_tea('milk tea', 'less sugar', 'normal ice', 'kiwi', 'tapioca')

# Arbitary keyword arguments
def user_profile(first, last, **add_info):
    """
    Build a dictionary containing user information
    """
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last

    for key, value in add_info.items():
        profile[key] = value
    
    return profile

#user = user_profile(
#    'john', 'smith', 
#    city='calgary', 
#    email='john.s@gmail.com')

#print(user)

