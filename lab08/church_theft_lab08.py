import matplotlib.pyplot as plt
def create_row(columns):
    d = {'start date' : columns[0], 'start time' : columns[1],
         'end date' : columns[2], 'end time' : columns[3],
         'text' : columns[4]}
    return d

file = open('/Users/Kylee/secu2002_YQKTH58/lab08/data/church_metal_theft.csv','r' )

spreadsheet = []
for line in file:
    # split line into columns
    columns = line.split(':::')
    row = create_row(columns)
    spreadsheet.append(row)
texts = [x['text'].lower() for x in spreadsheet]


lead_details = filter (lambda x: 'lead' in x, texts)
num_lead = len(lead_details)
print "The number of lead thefts:", num_lead
print ''

# Filtering and getting the free text details of all the thefts that involved copper being stolen
copper_details = filter (lambda x: 'copper' in x, texts)
# Counting the number of copper thefts
num_copper = len (copper_details)
print "The number of copper thefts:", num_copper
print ''

def pretty_month(months):
    d = {12 : 'December', 1 : 'January', 2 : 'February',
          3 : 'March', 4 : 'April', 5 : 'May',
          6 : 'June', 7 : 'July', 8 : 'August',
          9 : 'September', 10 : 'October', 11 : 'November'}
    pretty_months = []
    for m in months:
        if m in d:
            pretty_months.append(d[m])
        else:
            print 'entered an invalid month'
            return
    return pretty_months

months = dict.fromkeys(range(1,13),0)
lead_months = dict.fromkeys(range(1,13),0)
copper_months = dict.fromkeys(range(1,13),0)

for row in spreadsheet:
    # could also work according to end date
    start_date = row['start date']
    # date is as dd/mm/yyyy
    split_date = start_date.split('/')
    month = int(split_date[1])
    # count entry in both month it occurred
    months[month] += 1
    if 'lead' in row['text']:
        lead_months[month] += 1
    if 'copper' in row['text']:
        copper_months[month] += 1


xaxis_month = [12,11,10,9,8,7,6,5,4,3,2,1]
yaxis_lead = lead_months
yaxis_copper = copper_months
plt.bar(map(lambda x : x - 0.1, range(len(xaxis_month))), yaxis_lead,
align='center', color='blue', width=0.2)
plt.bar(map(lambda x : x + 0.1, range(len(xaxis_month))), yaxis_copper,
align='center', color='red', width=0.2)
plt.bar(map(lambda x : x - 0.1, range(len(xaxis_month))), months,
align='center', color='green', width=0.2)
plt.xlabel('Months in a year')
plt.xticks(range(len(xaxis_month)), xaxis_month, fontsize=10, rotation=90)
plt.ylabel('Number of crimes in each month')
plt.tight_layout()
plt.savefig('months.pdf')
plt.show()

