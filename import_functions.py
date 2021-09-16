# Importing specific functions - from module_name import function_name
# Giving functions an alias - 'as'
from functions_arbitrary_number import user_profile as profile

user1 = profile('jane', 'kennedy', city='toronto', email='jane.k@gmail.com', phone='9832738912')

print(user1)
