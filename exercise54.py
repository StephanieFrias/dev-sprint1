# This is where Exercise 5.4 goes
# Name: Stephanie Frias

def is_triangle(a,b,c):
	if a + b < c:
		print "no"
	elif a + c < b:
		print "no"
	elif b + c < a:
		print "no"
	else:
		print "yes"
is_triangle(4,5,7)

def triangle_sides():
	a=int(raw_input("length a?\n"))
	b=int(raw_input("length b?\n"))
	c=int(raw_input("length c?\n"))

is_triangle(4,8,9)

triangle_sides()