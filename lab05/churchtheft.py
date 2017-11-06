# Task 4
# To open the file and to display the data as lists, with each row as one element of the list
file = open('/Users/Kylee/secu2002_YQKTH58/lab04/data/church_metal_theft.csv','r' )
rows = file.readlines()

# To print an empty line in between
print ''
# To get the free texts of the crimes that occurred
free_text = []
for row in rows:
    free_text.append(row[48:])
# To convert all the data to lower case, as some are upper case
free_text_details = [x.lower() for x in free_text]
print "The free text details of all the thefts:", free_text_details

print ''
# Filtering and getting the free text details of all the thefts that involved lead being stolen
lead_details = filter (lambda x: 'lead' in x, free_text_details)
print "The free text details of all the lead thefts:" ,lead_details
# Counting the number of lead thefts
num_lead = len(lead_details)
print "The number of lead thefts:", num_lead
print ''

# Filtering and getting the free text details of all the thefts that involved copper being stolen
copper_details = filter (lambda x: 'copper' in x, free_text_details)
print "The free text details of all the copper thefts:" ,copper_details
# Counting the number of copper thefts
num_copper = len (copper_details)
print "The number of copper thefts:", num_copper
print ''

# Filtering and getting the free text details of the lead thefts that involved the lead flashing being stolen
leadflashing_details = filter (lambda x: 'flashing' in x, lead_details)
print "The free text details of all the lead flashing thefts:", leadflashing_details
# Counting the number of lead thefts that involved the lead flashing being stolen
num_leadflashing = len (leadflashing_details)
print "The number of lead flashing thefts:", num_leadflashing
print ''

# Filtering and getting the free text details of the lead thefts that involved roof parts being stolen
leadroofparts_details = filter (lambda x: 'roof' in x, lead_details)
print "The free text details of all the thefts involving parts of a lead roof:", leadroofparts_details
# Counting the number of lead thefts that involved roof parts being stolen     
num_partsofleadroof = len (leadroofparts_details)
print "The number of thefts involving parts of a lead roof:", num_partsofleadroof
print ''

# Convert list into sets
s1 = set(lead_details)
s2 = set(leadflashing_details)
s3 = set(leadroofparts_details)
# Finding the union of number of lead thefts involving lead flashing and roof parts
s4 = s2 | s3
# Finding the difference between the total number of lead thefts and the number of lead thefts involving lead flashing and roof parts
print "The set of lead thefts that involve neither lead flashing nor parts of a roof:", s1.difference(s4)
print "The number of lead thefts that involve neither lead flashing nor parts of a roof:",len(s1.difference(s4))

print ''
# Filtering and getting the free text details of all the thefts that involved roof parts being stolen
roof_details = filter (lambda x: 'roof' in x, free_text_details)
print "The free text details of all the thefts related to roofs:", roof_details
# Counting the number of thefts that involved roof parts being stolen
num_roof = len (roof_details)
print "The number of thefts related to roofs:", num_roof
print "Refer to church_theft.txt for explanation."

print ''
# Filtering and getting the free text details of all the copper thefts that involved lightning conductors / rods being stolen
lightningrod_details = filter (lambda x: 'rods' in x or 'rod' in x or 'conductor' in x or 'conducter' in x, copper_details)
print "The free text details of all the copper lightning rod / conductor thefts:", lightningrod_details
# Counting the number of copper thefts that involved lightning conductors / rods being stolen
num_lightningrod = len (lightningrod_details)
print "The number of copper lightning rod / conductor thefts:", num_lightningrod
print ''