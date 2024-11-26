import json

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)
