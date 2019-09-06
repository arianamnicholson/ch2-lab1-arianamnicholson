# Name: Ariana Nicholson
# Assignment title: Lab 1
# Time to complete: 45 min
# Description: This script calculates the rainfall in gallons on a small plot of land in a one inch rainstorm.
# Calculating the area of the plot of land in inches
lengthin = 50 * 12
widthin = 20 * 12
areain = (lengthin * widthin)
#print (areain)
#Calculating square inches of rainfall
rainfallin = 1
waterin = rainfallin * areain
#print (waterin)
#Converting square inches to gallons
watergal = (waterin * 0.004329)
#print (watergal)
#Printing the final results
print "lengthin is:", lengthin, "inches"
print "widthin is:", widthin, "inches"
print "areain is:", areain, "square inches"
print "waterin is:", waterin, "cubic inches"
print "watergal is:", watergal, "gallons"
