# Geometric Progression
c, d = None, None

def setup() :
  size(800, 800)
  smooth()
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))
  
def draw():
  global c, d
  background(253)
  stroke(0) 
  noFill()  
  constantFactor = 1.315
  circleSize = 20 
  
  for i in range(0,20):
    p = lerpColor(c, d, 1.0* i/width)
    stroke(p)
    #line(x, 0, x, height)
    
    #draws 20 concentric circles of decreasing diameter and decreasing lineWeight
    strokeWeight(circleSize/25.0) 
    ellipse(width/2,height, circleSize, circleSize)
    circleSize = circleSize * constantFactor 
    
def mousePressed():
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))

    
