import json
# Json(JavaScript Object Notation)
# json.dump(data, file object) - store data  
# json.load() - read data

def json_writer(data, filename):
    with open(filename, 'w') as f_w:
        json.dump(data, f_w)


def json_reader(filename):
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
        print(numbers)


filename = '1.basics/store_data/numbers.json'
numbers = [1, 2, 3, 4, 5, 6, 7]

json_writer(numbers, filename)
json_reader(filename)