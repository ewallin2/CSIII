import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv', 'r') as file:
    # Create a CSV reader object
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    
except FileNotFoundError:
    print("Packing list not found. Creating a new one.")
    with open('Homework3/packing_list.csv', 'w') as file:
        for row in data:
            file.writerow(row)
        