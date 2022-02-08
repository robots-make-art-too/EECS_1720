## note I changed between ring and rings and using semi-colons or not
# when uploading the version of code -- opps sorry.
# think of it as an exercise for your 100 Days of code ... make the codes consistent !

numRings = 40;
currentRing = 0;
rings = [0]*numRings # Declare the array;

colour = None;

def setup():
  size(300, 300);
  smooth();
  global numRings, colour;

  for i in range(numRings): 
    colour = color(random(255), random(255), random(255));
    rings[i] = Ring(0, 0, 0, False, colour); # Create each object

def draw():
  background(251,128,114);
  global numRings, rings;
  for i in range(numRings):
    rings[i].grow();
    rings[i].display();

# Click to create a new Ring
def mousePressed():
  global currentRing, numRings;
  rings[currentRing].start(mouseX, mouseY);
  currentRing+=1;
  if (currentRing >= numRings):
    currentRing = 0;

class Ring(object):
  def __init__(self, x, y, diameter, on, colour):
    self.x = x; # x-coordinate
    self.y = y; # y-coordinate
    self.diameter = diameter; # Diameter of the ring
    self.on = False; # Turns the display on and off
    self.colour = colour; # initial colour
    
  def start(self, xpos, ypos):
    self.x = xpos;
    self.y = ypos;
    self.on = True;
    self.diameter = 1;

  def grow(self):
    if (self.on == True):
      self.diameter += 1.5;
      if (self.diameter > 400):
        self.on = False;
  
  def display(self):
    if (self.on == True):
      noFill();
      strokeWeight(4);
      stroke(self.colour); #stroke(255, 153)
      ellipse(self.x, self.y, self.diameter, self.diameter);

  # def colour(self, colour1, colour2):
  #   self.colour1 = cclour1
  #   self.colour2 = colour2
