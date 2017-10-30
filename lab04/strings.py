# Task 1
mylist = ['h','e','l','l','o']

# Function: To join mysep and mylist
# Input: String (mylist), mysep " " to split on
# Output: mylist with " " (space) in between characters
def my_join (mylist, mysep = " "):
    word = ''
# Defining x as an element in the list, followed by iteration of x in the list, adding mysep " " (space) between each character as the output
    for x in mylist:
        word += x + mysep
    return word
# Printing the defined function
print my_join (mylist)

# Using the method join to combine mylist and mysep " " (space)
mysep = " "
print mysep.join(mylist)

# Using the method join to combine mylist and mysep1 "+"
mysep1 = "+"
print mysep1.join(mylist)

# Task 2
# Defining mystring
mystring = 'hello'

# Function: To change the string into a list, sorting the list alphabetically, and then joining the list back into a string
# Input: string (mystring)
# Output: alphabetically ordered string (mystring)
def sort_string(mystring):
    x = list(mystring)
    x.sort()
# Add an empty string to the front of the sorted list
    mynewstring = ''
    mynewstring = mynewstring.join(x)
    return mynewstring

# In a function, print the function name
print sort_string(mystring)


