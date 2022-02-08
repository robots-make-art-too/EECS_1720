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
  size(600,600);
  smooth();
  global numRings, ring;

  for i in range(numRings): 
    colour = color(random(255), random(255), random(255));
    ring[i] = Ring(0, 0, 0, False, colour); # Create each object




def draw():
  global numRings, rings;
  background(251,128,114)

  for i in range(numRings):
    ring[i].grow();
    ring[i].display();



def mousePressed():
 
 global numRings, rings;
  # when we click we want to activate a ring at the location of the cursor
  # so our xpos = mouseX
  # and the ypos = mouseY
  ring[currentRing].start(mouseX, mouseY);

  currentRing += 1;
  if (currentRing >= numRings):
    currentRing = 0;




class Ring(object):
  # what attributes, or characteristics
  # do we want our rings to have?
	# 1. initialize
  def __init__(self, x, y, diameter, on, colour):
    self.x = x;
    self.y = y;
    self.diameter = diameter;
    self.on = False;
    self.colour = colour;

  # 2. start
	def start(self, xpos, ypos):
    self.x = xpos;
    self.y = ypos;
    self.on = True;
    self.diameter = 1;

  # 3. grow
  def grow(self):

    if (self.on == True):
      self.diameter += 1.5
      if (self.diameter > 400):
        self.on = False

  # 4. display
  def display(self):

    if (self.on == True):
      noFill()
      strokeWeight(4)
      stroke(self.colour) #stroke(255, 153)
      ellipse(self.x, self.y, self.diameter, self.diameter)


# note: we need this object to know about
# _ its own self_, so _it_ can make
# changes to its _self_