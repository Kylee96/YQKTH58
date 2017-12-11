from datetime import datetime as dt
import csv
import utilities
# Opening the file
file = open('/Users/Kylee/secu2002_YQKTH58/lab09/data/shapeshift.csv','r')
r = csv.DictReader(file)
# Parsing the date as a list of dictionaries
date_list = []
for rows in r:
    new_date = dt.fromtimestamp(float(rows['timestamp'])).date()
    rows['timestamp'] = new_date
    date_list.append(rows)
    date_list= sorted(date_list, key=lambda x:x['timestamp'])


# Task 4(1)
print 'Linear searching for entries in the dataset that occurred on 5 October 2017 (05/10/2017):'
utilities.lin_find(date_list, "05/10/2017")
print ''
print 'Binary searching for entries in the dataset that occurred on 5 October 2017 (05/10/2017):'
utilities.bin_find(date_list, "05/10/2017")
print ''
# Task 4(2)
print 'Linear searching for entries in the dataset that occurred on 12 November 2017 (12/11/2017):'
utilities.lin_find(date_list, "12/11/2017")
print ''
print 'Binary searching for entries in the dataset that occurred on 12 November 2017 (12/11/2017):'
utilities.bin_find(date_list, "12/11/2017")
print ''
# Task 4(3)
print 'Linear searching for entries in the dataset that occurred on 2 December 2017 (02/12/2017):'
utilities.lin_find(date_list, "02/12/2017")
print ''
print 'Binary searching for entries in the dataset that occurred on 2 December 2017 (02/12/2017):'
utilities.bin_find(date_list, "02/12/2017")