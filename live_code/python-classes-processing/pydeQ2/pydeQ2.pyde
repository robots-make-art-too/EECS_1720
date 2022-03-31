# I run in processing -- but please rename me to test.py when you are done and then edit the clean version: yourcopy.pyde
# you should probably rename yourcopy.pyde to pydeQ2.pyde when you are ready to run!

###
# what do we need for our concept?
# we list 4 main components: variables, setup, interactivity(? it could be our robot flare?), the class ClassyRobot(object):
###

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# THE VARIABLES
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 1. My variables, and what I need them to do:
#
# a way to count the robots
numRobots = 17 # = ?;

# a way to store the robots
robots = [0]*numRobots;

# a way to keep track of which robots
currentRobot = 0; # arrays start at a value of 0 so we will too

# a way to change the robot's flare?
# do they have colour?
# colour = None;
# do they have sound?
# what else? (we know they have shapes!)

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# THE STANDARD SETUP, DRAW
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 2. how to setup: setup(), draw() - like always
def setup():
  size(600,600); # bigger? smaller?
  smooth();
  global numRobots, robots;
  for i in range(numRobots):
    colour = color(random(255), random(255), random(255)); # I don't think the robots want to cycle through random colours though
    robots[i] = ClassyRobot(0, [], False, 'abcdef', 2, 2); # Create each object with initial parameters (but how many are there?)

def draw():
  global numRobots, robots;
  background(251,128,114); # that pinkish background colour
  # hmm.. what *is* a good photo colour for the background of a robot family photo?
  # or did you want to take it outside? infront of a tree?
  img = loadImage("img.png")
  # image(img, 0, 0)
  image(img, 0, 0, width/3, height/3)

  for i in range(numRobots):
    # this checks each robot object that could possibly exist
    # if there are any conditions attributes
    # robots[i].?? # maybe you defined some other conditions in your class ClassyRobot()
    robots[i].display(); # the draw conditions _I_ defined in class ClassyRobot()

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# FLARE? INTERACTION? SAVING A PICTURE?
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 3a. do you want some interactivity?
# I'm not sure you'll want to use anything like this function but maybe you find it interesting?
def mousePressed():
  global numRobots, currentRobot;
  robots[currentRobot].start(mouseX, mouseY,); # start is an activation _I_ defined in class ClassyRobot(object)
  currentRobot += 1;
  if (currentRobot >= numRobots):
    currentRobot = 0;
  name(currentRobot);

# 3b. do we need to save a file?
def save(i):
  global numRobots;
  with open('data/myfile.txt', 'a+') as textFile:
    textFile.write("\nRobot %s name is:" %i + robots[i].name) # ? how are you storing the robot's attributes?
    # textFile.write("\nThe profile_use_background_image is : " + str(robot.profile_use_background_image)) # do you need a str(ing)?
    # maybe you should make a list of the attributes you should keep track of first, then build the class...?

def load(i):
  pass;

def name(i):
  global numRobots, currentRobot;
  # what about just print to screen? Is there a way to do that _encapsulated_ into the class ClassyRobot()? hmmm ....
  robots[i].name = 'shh' # I am just a placeholder
  print('My name is: `%s`' %i, robots[i].name);
  if currentRobot > 5:
    robots[currentRobot].shbam = True;
  else:
    save(i);  # do we need to save a file?
    load(i); # or load one?

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# THE CLASS
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 4. OOP setup for a python class
class ClassyRobot(object):
  # we need to ask ourselve: what attributes, or characteristics do we want our robots to have?
  # also, how do we know what is a child and what is a parent?

  # 4a. initialize -> think of me as a 1-to-1 with def setup()
  # I am needed for an instance of class to exist ( I self, therefore I am )
  def __init__(self, param, params, shbam, name, x, y):
    self.param = param;
    self.params = params;
    self.shbam = shbam;
    self.name = name; # this could be useful
    self.x = x;
    self.y = y;
    #...;

  # 4b. an example of giving a class some activation
  # start -> think of me as a 1-to-1 with the interaction - def mousePressed()
  def start(self, xpos, ypos):
    self.x = xpos;
    self.y = ypos;
    #...

  # 4c. display -> think of me as a 1-to-1 with def draw():
  # I do need that family photo afterall...
  def display(self):
    if (self.shbam == True):
      noFill();
      strokeWeight(4);
      stroke(255, 153);
      # stroke(self.colour);
      line(self.x, self.y, 5, 5);
      # don't we have to give the robots a shape?
      # ellipse(self.x, self.y, self.diameter, self.diameter);

  # 4d. assigning some flare?
  # randomly? specifically? inherited?
  # are we passing in any parameters?

  #def gimmeFlare(self, flare):
    #self.flare = flare; # you can use this method or try another way if you want to use this

  # did you want to add sound? try it here and follow the pattern from Week 04
  # maybe you want to initialize something in def __init__(): ?
  def sound():
    pass # place holder until you think of something to add or not
