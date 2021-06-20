import csv

def timetable(x, y):
    x = int(input)
    y = int(input)
    for x in range(50):
        product = x * y
        result = product
    return result

def timetable(x, y):
    if x < y:
        return x
    return y

def love(name):
    first_name = input("Enter your first name: ")
    middle_name = input("Enger your middle name: ")
    last_name = input("Enter your last name: ")
    name = first_name +" "+ middle_name + " "+ last_name
    return name

def read_me(file_name):
    with open(file_name) as file:
        read_file = list(csv.reader(file))
    return read_file

def add(x, y):
    if x < y:
        sum = x + y
    if y < x :
        diff = y - x
        return diff
    return sum

def fun(name):
    name = input("Enter your name: ")
    return name



