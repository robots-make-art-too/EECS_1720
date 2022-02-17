# Put it together
add_library('sound')

c, d, ch_1, ch_2 = None, None, None, None

def setup() :
  size(800, 800)
  
  smooth()
  
  global ch_1, ch_2
  ch_1 = SinOsc(this)
  ch_1.play(0,1)
  ch_2 = SinOsc(this)
  ch_2.play(0,1)  
   
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))


def draw():
  global ch_1, ch_2, c, d
  background(253)
  stroke(0) 
  noFill()  
  constantFactor = 1.315
  circleSize = 20 
  
  if mousePressed:
    ch_1.set(400, 1, 0, 0)
    ch_2.set(401, 1, 0, 0)
    
    # timer?? 
    
    for i in range(0,20):
        p = lerpColor(c, d, 1.0* i/width)
        stroke(p)
        #line(i, 0, i, height)

        #draws 20 concentric circles of decreasing diameter and decreasing lineWeight
        strokeWeight(circleSize/25.0) 
        ellipse(width/2,height, circleSize, circleSize)
        circleSize = circleSize * constantFactor
        
  else:
    ch_1.set(0, 1, 0, 0)
    ch_2.set(0, 1, 0, 0)    
   
   
def mousePressed():
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))
  ch_1.set(400, 1, 0, 0)
  ch_2.set(401, 1, 0, 0)

    
