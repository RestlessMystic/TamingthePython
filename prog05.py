#
#	Taming the Python
#	Govind Maheswaran
#	Example Programs


#	Prog 05
#	Program to demonstrate some String Operations

str1 = raw_input("Enter first string : ")
str2 = raw_input("Enter second string : ")

print "Checking if second string is substring of circulated first string"
str1 = str1 + str1
if str2 in str1:
	print "Yes"
else:
	print "No"