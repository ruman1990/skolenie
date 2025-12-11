import csv

with open('names.csv', 'w',newline='') as f:
    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter='|')
    writer.writeheader()
    writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
    writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})