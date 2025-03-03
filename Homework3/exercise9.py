import csv

with open('Homework3/Bestseller - Sheet1.csv', 'r') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  for row in csv_reader:
    max_sales = 0
    max_sales_index = 0
    if row[4] > max_sales:
        max_sales_index = i
        max_sales = row[4]
    max_sales_row = csv_reader[max_sales_index]

with open('Homework3/bestseller_info.csv', 'w', newline='') as file:
  file.writerow(max_sales_row)


      
