import csv
f = open('/Users/Kylee/secu2002_YQKTH58/lab07/data/church_metal_theft.csv','r' )
r = csv.DictReader(f, delimiter ='|')
spreadsheet = []
for row in r:
    spreadsheet.append(row)
print spreadsheet