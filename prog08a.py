#
#	Taming the Python
#	Govind Maheswaran
#	Example Programs


#	Prog 08a
#	Program to demonstrate a simple function

def sum(a,b):
	return(a+b);
	
c = sum(5,8)
print c
print sum(9,12)
print sum(int(raw_input("Enter a number")),1)