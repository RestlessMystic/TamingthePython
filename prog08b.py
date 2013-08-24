#
#	Taming the Python
#	Govind Maheswaran
#	Example Programs


#	Prog 08a
#	Program to demonstrate a  function

def fibonacci(n):
	a=0; b=1;
	while a<n:
		print a
		a,b= b,a+b
	

fibonacci(int(raw_input("Enter Max Value : ")))