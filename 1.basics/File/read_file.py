# Reading file
# open() - open the file to access it
# read() - read the file
# 'with' keyword - closes the file once access to it is no longer needed.

with open('note.txt') as file_o:
    contents = file_o.read()
    print(contents)

# File paths
file_path = '1.basics/File/hello_world.txt'
with open(file_path) as file:
    contents = file.read()
    print(contents)

# Reading line by line - after each line, there are blank line
print('\nReading line by line')
with open(file_path) as file:
    for line in file:
        print(line.rstrip())

# Making a list of lines
print('\nMaking a list of lines from a file')
with open(file_path) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())