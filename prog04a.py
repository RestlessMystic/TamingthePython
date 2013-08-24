#
#	Taming the Python
#	Govind Maheswaran
#	Example Programs


#	Prog 04a
#	Program to demonstrate while loop

Running = True;

while(Running):
	age = int(raw_input("Enter age : "))
	if age==18:
		print "You are now Eligible for Voting"
	elif age>18:
		print "You are already Eligible for Voting"
	else:
		print "You still gotta wait, Kiddo"
	ask = raw_input("Do you want to continue(y/n) : ")
	if ask is "n":
		Running = False
	elif ask is "y":
		Running = True
	
