import math

class complex():
	def __init__(self,r,i):
		self.i=i
		self.r=r
		
	def abs(self):
		return math.sqrt(self.r**2 + self.i**2)
		
	def real(self):
		return self.r
		
	def imag(self):
		return self.i
	
	def __add__(self, number):
		return (complex(self.r + number.r, self.i + number.i))
	
	def __sub__(self, number):
		return complex(self.r - number.r, self.i - number.i)
		
	def __mul__(self, number):
		return complex(self.r*number.r - self.i*number.r, self.r*number.i + self.i*number.r)
		
	def __truediv__(self, number):
		real = (self.r*number.r + self.i*number.r)/(number.r**2 + number.i**2)
		im = (self.r*number.i - self.i*number.r)/(number.r**2 + number.i**2)
		return complex(real, im)
	
	def conjugate(self):
		return complex(self.r, -1 * self.i)
	
	"""print command"""
	def __str__(self):
		return (str(self.r) + " + (" + str(self.i) + ")i")
		
	def argument(self):
		arg = math.degrees(math.atan(self.i/self.r))
		
		if self.r>0:
			return arg
		elif self.r<0 and self.i>=0:
			return (180+arg)
		elif self.r<0 and self.i<0:
			return (arg-180)
		elif self.r==0 and self.i<0:
			return -90
		elif self.r==0 and self.i>0:
			return 90
		elif self.r==0 and self.i==0:
			return str("Indeterminate")
		
class ccal():
			
	print("Enter first number:")
	a=float(input("Enter real part: "))
	b=float(input("Enter imaginary part: "))
	c1 = complex(a,b)

	print("Enter second number:")
	a=float(input("Enter real part: "))
	b=float(input("Enter imaginary part: "))
	c2 = complex(a,b)	

	"""Sample flow of program."""
	choice=1
	while choice!=0:
		print("0. Exit")
		print("1. Add")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division")
		print("5. Absolute of 1st complex number")
		print("6. Print 1st complex number")
		print("7. Conjugate of 1st complex number")
		print("8. Argument of 1st complex number")
		choice=int(input("Enter choice: "))
		if choice==1:
			print("Result: ",c1+c2)
		elif choice==2:
			print("Result: ",c1-c2)
		elif choice==3:
			print("Result: ",c1*c2)
		elif choice==4:
			print("Result: ",c1/c2)
		elif choice==5:
			print("Result: ",c1.abs())
		elif choice==6:
			print("Result: ")
			print(c1)
		elif choice==7:
			print("Result: ")
			print(c1.conjugate())
		elif choice==8:
			print("Result: ",c1.argument())
		elif choice==0:
			print("Exiting!")
		else:
			print("Invalid choice!!")
