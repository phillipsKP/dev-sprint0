from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t, length, delay):
	t=Turtle()
	t.delay = 0.01
	for zz in range(4):
		fd(t,length)
		lt(t)


square(bob,50, 0.01)

wait_for_user()


