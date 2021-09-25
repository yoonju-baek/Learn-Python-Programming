# Json(JavaScript Object Notation)
# json.dump(data, file object) - store data  
# json.load() - read data

import json

def json_writer(data, filename):
    with open(filename, 'w') as f_obj:
        json.dump(data, f_obj)


def json_reader(filename):
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
        print(numbers)


filename = '1.basics/File/numbers.json'
numbers = [1, 2, 3, 4, 5, 6, 7]

json_writer(numbers, filename)
json_reader(filename)