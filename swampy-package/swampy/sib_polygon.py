# Polygon excercise from Week 0

# Name: Kevin Phillips


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				


def polygon(t,length,n):
	t=Turtle()
	t.delay = (0.01)
	for iiiii in range(n):
		fd(t,length)
		lt(t, 360/n)

polygon(bob,75,5)	





wait_for_user()					
