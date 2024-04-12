import csv

def input_read(csv_file_name):
    with open(csv_file_name, newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        numbers = []
        for row in file_reader:
            numbers.append(', '.join(row))

    return numbers[1:]