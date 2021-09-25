# Pass the exception

def count_characters(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        characters = len(contents)
        print("The file " + filename + " has " + str(characters) + " characters.")

file_path = '1.basics/File/'
filenames = ['favorite_lang.txt', 'vote.txt', 'hello_world.txt']

for filename in filenames:
    count_characters(file_path + filename)
