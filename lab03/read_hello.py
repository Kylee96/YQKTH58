# Opening the file
f = open('/Users/Kylee/secu2002_YQKTH58/lab03/data/hello_world.txt', 'r')
# For loop for reading and printing the first 4 characters of each line
for line in f:
    print line[:4]