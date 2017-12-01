# To open the file and to display the data as lists, with each row as one element of the list
file = open('../../../../data/church_metal_theft.csv','r' )
rows = file.readlines()
#print rows

# To print an empty line in between
print ''
months = []
for row in rows:
    months.append(row[3:5])

# To write a function to count the number of crimes in each month
def counting_months (x):
    occurrences = 0
    for i in months:
        if x == i:
            occurrences += 1
    return occurrences

# To print the number of crimes in each month
print "Number of crimes in January:", counting_months('01')
print "Number of crimes in February:", counting_months('02')
print "Number of crimes in March:", counting_months('03')
print "Number of crimes in April:", counting_months('04')
print "Number of crimes in May:", counting_months('05')
print "Number of crimes in June:", counting_months('06')
print "Number of crimes in July:", counting_months('07')
print "Number of crimes in August:", counting_months('08')
print "Number of crimes in September:", counting_months('09')
print "Number of crimes in October:", counting_months('10')
print "Number of crimes in November:", counting_months('11')
print "Number of crimes in December:", counting_months('12')

# Making the number of crimes per month into a list
months_list = [counting_months('01'), counting_months('02'), counting_months('03'), counting_months('04'), counting_months('05'),counting_months('06'), counting_months('07'), counting_months('08'), counting_months('09'),counting_months('10'),counting_months('11'), counting_months('12')]
# Making a dictionary, mapping keys (Month names) to values (number of crimes for that respective month)
months2 = {'January' : [counting_months('01')], 'February' : [counting_months('02')],
           'March' : [counting_months('03')], 'April' : [counting_months('04')],
           'May' : [counting_months('05')], 'June' : [counting_months('06')],
           'July' : [counting_months('07')], 'August' : [counting_months('08')],
           'September' : [counting_months('09')], 'October' : [counting_months('10')],
           'November' : [counting_months('11')], 'December' : [counting_months('12')]}

# Function to obtain the corresponding key (Month name)
def getkey(dictionary_name, value):
    for key, val in months2.items():
        if val == value:
            return key
# Function to obtain the corresponding key (Month name) if there is more than 1 and value is minimum
def getkey1 (dictionary_name, value):
        min_value = min(months2.values())
        keys_list = [key for key, val in months2.items() if val == min_value]
        return keys_list

# Printing a blank line
print ''
# Printing the maximum number of crimes and the corresponding month it occurred in
print 'The maximum number of crimes is', max(months2.values()), 'and it occurred in', getkey(months2, max(months2.values()))
# Printing the minimum number of crimes and the corresponding months it occurred in
print 'The minimum number of crimes is', min(months2.values()), 'and it occurred in', getkey1(months2, min(months2.values()))

#Printing a blank line
print ''
# Putting the seasons into a list
seasons = [ 'Winter', 'Spring', 'Summer', 'Autumn']
# Creating a dictionary mapping the seasons to the number of crimes that occurred in the months that are in the seasons
seasons_dict = {'Winter' : [counting_months('12'), counting_months('01'), counting_months('02')],
           'Spring' : [counting_months('03'), counting_months('04'), counting_months('05')],
           'Summer' : [counting_months('06'), counting_months('07'), counting_months('08')],
           'Autumn' : [counting_months('09'), counting_months('10'), counting_months('11')]}

# To find the sum of each value and to link it to their respective keys
for key in seasons_dict:
    seasons_dict[key] = sum(seasons_dict[key])
# Function to obtain the corresponding key (Season name)
def getkey(seasons_dict, value):
    for key, val in seasons_dict.items():
        if val == value:
            return key

# Printing the number of crimes for each season
print 'The number of crimes for each respective season is', seasons_dict
# Printing the maximum number of crimes and the corresponding season it occurred in
print 'The maximum number of crimes per season is', max(seasons_dict.values()),  'in', getkey(seasons_dict, max(seasons_dict.values()))
# Printing the minimum number of crimes and the corresponding season it occurred in
print 'The minimum number of crimes per season is',  min(seasons_dict.values()), 'in', getkey(seasons_dict, min(seasons_dict.values()))

