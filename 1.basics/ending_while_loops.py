# User enter 'quit' to end the program
prompt = "Tell me something. If you want to end the program, enter 'quit': "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Using a flag to end the program
prompt = "(Using a flag)Tell me something. If you want to end the program, enter 'quit': "

active = True
while active:
    msg = input(prompt)

    if msg == 'quit':
        active = False

    else:
        print(msg)