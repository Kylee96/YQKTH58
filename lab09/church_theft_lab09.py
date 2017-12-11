import csv
from datetime import datetime as dt
import utilities
f = open('/Users/Kylee/secu2002_YQKTH58/lab07/data/church_metal_theft.csv','r' )
r = csv.DictReader(f, delimiter ='|')
spreadsheet = []
for row in r:
    spreadsheet.append(row)
    date = dt.strptime(row['start date'], '%d/%m/%Y').date()
    spreadsheet = sorted(spreadsheet, key=lambda x: x['start date'])

print 'Linear searching for entries in the dataset that occurred on 26 February 2011 (26/02/2011):'
utilities.lin_find_1(spreadsheet,"26/02/2011")
print ''
print 'Linear searching for entries in the dataset that occurred on 06 July 2009 (06/07/2009):'
utilities.lin_find_1(spreadsheet,"06/07/2009")
print ''
print 'Linear searching for entries in the dataset that occurred on 22 April 2013 (22/04/2013):'
utilities.lin_find_1(spreadsheet,"22/04/2013")
print ''
print 'Linear searching for entries in the dataset that occurred on 15 November 2010 (15/11/2010):'
utilities.lin_find_1(spreadsheet,"15/11/2010")

print ''
print 'Binary searching for entries in the dataset that occurred on 26 February 2011 (26/02/2011):'
utilities.bin_find_1(spreadsheet,"26/02/2011")
print ''
print 'Binary searching for entries in the dataset that occurred on 06 July 2009 (06/07/2009):'
utilities.bin_find_1(spreadsheet,"06/07/2009")
print ''
print 'Binary searching for entries in the dataset that occurred on 22 April 2013 (22/04/2013):'
utilities.bin_find_1(spreadsheet,"22/04/2013")
print ''
print 'Binary searching for entries in the dataset that occurred on 15 November 2010 (15/11/2010):'
utilities.bin_find_1(spreadsheet,"15/11/2010")
