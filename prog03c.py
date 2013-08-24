#
#	Taming the Python
#	Govind Maheswaran
#	Example Programs


#	Prog 03c
#	Program to demonstrate If-Elif-Else

age = int(raw_input("Enter age : "))
if age==18:
	print "You are now Eligible for Voting"
elif age>18:
	print "You are already Eligible for Voting"
else:
	print "You still gotta wait, Kiddo"
