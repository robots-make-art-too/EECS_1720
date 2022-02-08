# Python - processing.py

#
# 2. rings:
# a way to count the rings
numRings = 40

#	a way to store the rings
ring = [0]*numRings

#	keep track of which rings
currentRing = 0
# arrays start at a value of 0

# to change the ring colours
colour = None




# 1. how to setup: setup(), draw()
def setup():
  size(600,600)
  smooth()
  global numRings, ring

  # for i in range(numRings): 
  #   colour = color(random(255), random(255), random(255))
  #   rings[i] = Ring(0, 0, 0, False, colour) # Create each object


def draw():
  global numRings, rings



def mousePressed():
  global numRings, rings




class Ring(object):
# what attributes, or characteristics
# do we want our rings to have?
	# 1. initialize
  def __init__(self):

# 2. start
	def start(self):


# 3. grow
  def grow(self):


# 4. display
  def display(self):


# note: we need this object to know about
# _ its own self_, so _it_ can make
# changes to its _self_