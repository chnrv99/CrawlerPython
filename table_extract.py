import csv
csv_filename = 'link-1.csv'
with open(csv_filename) as f:
    reader = csv.reader(f)
    lst = list(tuple(line) for line in reader)
print(lst)