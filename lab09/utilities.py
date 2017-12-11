# Task 1
"""
data = [1, 2, 4, 5, 6, 7, 9, 12, 17, 19]
e = 7

# LIN_FIND: To do a linear search in a list to see if the variable is present
# Input: List and variable
# Output: Variable if it is present, and the number of times taken to search

def lin_find (data_list,num):
    # Counting the number of times the linear search occurs
    count = 0
    # Setting up a for loop to check if the variable is in the list
    for x in data_list:
        # Adding one to the counter everytime a search is done in the loop
        count += 1
        if x == num:
            # Returning the entry if it is in the list
            print 'The entry that is present in the list:', x
            break
        else:
            print 'The entry is not present in the list.'
    print 'The number of times with linear search:', count

# Trying out the function with our example
lin_find(data,e)


# Task 2
data = [1, 2, 4, 5, 6, 7, 9, 12, 17, 19]
e = 7

# BIN_FIND: To do a binary search in a list to see if the variable is present
# Input: List and variable
# Output: Variable if it is present, and the number of times taken to search

def bin_find (data_list, num):
    first = 0
    last = len(data_list)-1
    loop_count = 0
    while first != last:
        if data_list[(first+last) //2] == num:
            loop_count += 1
            print 'The entry that is present in the list:', num
            print 'The number of times it goes through a loop:', loop_count
            return None
        elif data_list[(first+last) //2] < num:
            first = [(first+last) //2] + 1
            loop_count += 1
        elif data_list[(first+last) //2] > num:
            last = data_list[(first+last) //2] - 1
            loop_count += 1
        else:
            print 'This entry is not present in the list'
            print 'The number of times it goes through a loop:', loop_count
            return None
print ''

# Trying out the function with our example
bin_find(data,e)

"""

# Task 4
# Importing the module datetime
from datetime import datetime as dt

def lin_find(data,date):
    # Counting the number of times the linear search occurs
    count = 0
    # Converting the string into the date format
    date= dt.strptime(date,'%d/%m/%Y').date()
    # Dealing with a list of dictionaries
    for dictionary in data:
        if dictionary['timestamp'] == date:
            # Returning the entry if it is in the list and adding 1 to the counter
            count += 1
            print 'The entry that is present in the list:', dictionary
    if count == 0:
        print "There are no entries present in the list."
    print 'The number of times with linear search:', count


def bin_find(data,date):
    first = 0
    last = len(data)-1
    loop_count = 0
    # Converting the string into the date format
    date= dt.strptime(date,'%d/%m/%Y').date()
    for dictionary in data:
        while first != last:
            if data[(first + last) // 2]['timestamp'] == date:
                loop_count += 1
                print 'The entry that is present in the list:', dictionary
                print 'The number of times it goes through a loop:', loop_count
                return None
            elif data[(first+last)//2]['timestamp'] < date:
                print data[(first+last)//2]['timestamp']
                first = (first + last) //2
                loop_count += 1
            elif data[(first+last)//2]['timestamp'] > date:
                last = (first + last) //2
                loop_count += 1
            else:
                loop_count += 1
                print 'This entry is not present in the list'
                print 'The number of times it goes through a loop:', loop_count
                return None
    print ''


# Task 5
def lin_find_1(data,date):
    # Counting the number of times the linear search occurs
    count = 0
    # Converting the string into the date format
    for dictionary in data:
        if dictionary['start date'] == date:
            count += 1
            # Returning the entry if it is in the list
            print 'The entry that is present in the list:', dictionary
    if count == 0:
        print "There are no entries present in the list."
    print 'The number of times with linear search:', count


def bin_find_1(data,date):
    first = 0
    last = len(data)-1
    loop_count = 0
    # Converting the string into the date format
    date= dt.strptime(date,'%d/%m/%Y').date()
    while first != last:
        if data[(first + last) // 2]['start date'] == date:
            loop_count += 1
            print 'The entry that is present in the list:', date
            print 'The number of times it goes through a loop:', loop_count
            return None
        elif data[(first+last)//2]['start date'] < date:
            print data[(first+last)//2]['start date']
            first = (first + last) //2 +1
            loop_count += 1
        elif data[(first+last)//2]['start date'] > date:
            last = (first + last) //2 -1
            loop_count += 1
        else:
            loop_count += 1
            print 'This entry is not present in the list'
            print 'The number of times it goes through a loop:', loop_count
            return None
print ''