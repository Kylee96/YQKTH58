import csv
f = open('/Users/Kylee/secu2002_master/data/london_gang_attr.csv','r' )
r = csv.DictReader(f, delimiter =',')
age_data = []
arrests_data = []
convictions_data = []
prison_data = []
for rows in r:
    age_data.append(rows['Age'])
    arrests_data.append(rows['Arrests'])
    convictions_data.append(rows['Convictions'])
    prison_data.append(int(rows['Prison']))

age_list = [int(num) for num in age_data if num]
mean_age = sum(age_list) / float(len(age_list))
print 'The mean age of the gang:', mean_age
print ''

min_age = min(age_list)
max_age = max(age_list)
print 'The age range of the gang:', min_age, 'to', max_age

arrests_list = [int(num) for num in arrests_data if num]
sum_arrests = sum(arrests_list)
print ''
print 'The total number of arrests across all gang members:', sum_arrests

convictions_list = [int(num) for num in convictions_data if num]
sum_convictions = sum(convictions_list)
print ''
print 'The total number of convictions:', sum_convictions

sum_prison = sum(prison_data)
print ''
print 'The totla number of members who have spent time in prison:', sum_prison