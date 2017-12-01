# Task 1
import random
x = random.sample(range(0,500),100)
print 'Sample x:', x
y = random.sample(range(0,500),100)
print 'Sample y:', y

# Task 2
# Expect their respective means to be 250 each, both the same
# Hypothesis: There is a difference in the means of x and y
# Null hypothesis: There is no difference in the means of x and y
import scipy.stats as ss
print ''
v = ss.ttest_rel(x,y)
print v

# If the pvalue is more than 0.05, we cannot reject the null hypothesis
# Although the pvalue changes everytime we run it due to different samples of 100 numbers, the pvalue is nearly always more than 0.05
# Thus, we can conclude that there is no difference in the means of x and y

# Task 3
print ''
a = ss.linregress(x,y)
print a
# The rvalue = Since the rvalue is always near to 0, we can conclude that there is no correlation between x and y
# The pvalue = Since the pvalue is always higher than 0.05, we cannot reject the null hypothesis and can conclude that there is no difference in the means of x and y
# The pvalue is expected but the rvalue is not expected as we expected a correlation between x and y

# Task 4
print ''
import matplotlib.pyplot as plt
xaxis = x
yaxis = y
colors = []
# Plotting the data according to the color
for y in yaxis:
    if y > 250:
        colors.append('red')
    else:
        colors.append('blue')
plt.scatter(xaxis, yaxis, c=colors)
plt.xlim([-5,505])
plt.ylim([-5,505])
# Saving the variables slope and intercept
slope = a.slope
intercept = a.intercept
# Plotting the best fit line
xaxis = range(500)
yaxis = [slope*x + intercept for x in xaxis]
plt.plot(xaxis,yaxis)
plt.savefig('plot.pdf')
plt.show()
