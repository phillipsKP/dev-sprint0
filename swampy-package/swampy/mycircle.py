from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay=0.02

def polygon(t,length,n):
	t=Turtle()
	#t.delay = (0.01)
	for iiiii in range(n):
		fd(t,length)
		lt(t, 360/n)
polygon(bob, 50, 8)

world.clear()
"""
#gen's solution for reference
def circle(turtle,radius):
 	circumference = 2 * pi * radius
	factor = radius/5
	sides = int(circumference/factor)
	length = circumference / sides
	polygon(turtle,length,sides)

circle(bob,20)

wait_for_user()
"""
#from math import *
def circle(t,r):
	#t = Turtle()
	circum = 2 * pi * r
	n = 50 
	length = circum / n
	polygon(t,length,n)		
circle(bob,100)


wait_for_user()
	