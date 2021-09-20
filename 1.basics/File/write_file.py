# Writing to a file
# open(filename, mode) - mode: r(read)-default, w(write), a(append), r+(rw)
# write() - write to the file
file_path = '1.basics/File/'
filename = 'favorite_lang.txt'

with open(file_path+filename, 'w') as file_object:
    file_object.write("I love Python.\n")
    file_object.write("I love Java.\n")