kms_in_miles = 1.61
miles_in_kms= 1/1.61
print 1/1.61
num_miles_in_kms = 0.8 * (1/1.61)

print "800 meters 0.8km ; 0.8km is", num_miles_in_kms, "miles"

secs_in_min = 60
time_in_secs= 2* secs_in_min + 10
print time_in_secs

print "800m in 2min10secs is", num_miles_in_kms, "miles in", time_in_secs, "seconds"
secs_per_mile = (1* time_in_secs) / num_miles_in_kms
print secs_per_mile

mins_per_mile = secs_per_mile / secs_in_min
print mins_per_mile

mins_per_mile = secs_per_mile / secs_in_min

#Because we want it to be expressed 8:30 minutes per mile, rather than 8.5 minutes per mile, we need separate expressions for minutes and seconds
exact_mins = int(mins_per_mile)
seconds_left = secs_per_mile % secs_in_min

print exact_mins, ":", int(seconds_left),"minutes per mile"

