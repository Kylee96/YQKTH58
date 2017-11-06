# Task 1
# Loop_filter: Goes thru the list and filters out variables that satisfy the condition of being > x
# Input: List of items, condition
# Output: List of variables that satisfy the condition
def loop_filter(list, x):
    newlist = []
    for y in list:
        if y > x:
            newlist.append(y)
# The return statement should always be outside the for loop
    return newlist
print loop_filter([33,67,2,89,100,957],50)

# Task 2
# Writing a one line function, lambda to specify the condition
a = filter(lambda x : x > 43, [18,23,36,48,50,69,72,80])
print a
