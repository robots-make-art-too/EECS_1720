// Sound, Image, Interaction

let p;
let c, d;

let trigger = 0;
let autoplay = false;
let osc;

// The midi notes of a scale
let notes = [ 60, 62, 64, 65, 67, 69, 71];


function setup() {
  createCanvas(800, 800);
  smooth(); 

  c= color(random(255), random(255), random(255));
  d= color(random(255), random(255), random(255));

  // A triangle oscillator
  osc = new p5.TriOsc();
  // Start silent
  osc.start();
  osc.amp(0);
}

function draw() {
  background(253);
  stroke(0); 
  noFill();
  
  var constantFactor = 1.315;
  var circleSize = 20; 
  
  //draws 20 concentric circles of decreasing diameter and decreasing lineWeight
  if (mouseIsPressed === true) {

    for (let i=1; i<20; i++) {

      //loop through every x
      
      p = lerpColor(c, d, 1.0*i/width);
      stroke(p);
      // line(i, 0, i, height); //draw a vertical line at every x

      strokeWeight(circleSize/25.0); 
      ellipse(width/2,height, circleSize, circleSize);
      circleSize = circleSize * constantFactor; 
    } // end of for 
  } // end of if mouseIsPressed()
} // end of function draw()


// A function to play a note
function playNote(note, duration) {
  osc.freq(midiToFreq(note));
  // Fade it in
  osc.fade(0.5,0.2);

  // If we sest a duration, fade it out
  if (duration) {
    setTimeout(function() {
      osc.fade(0,0.2);
    }, duration-50);
  }
}


// When we click
function mousePressed(event) {

  c= color(random(255), random(255), random(255));
  d= color(random(255), random(255), random(255));
 
  if(event.button == 0 && event.clientX < width && event.clientY < height) {
    // Map mouse to the key index
    let key = floor(map(mouseX, 0, width, 0, notes.length));
    playNote(notes[key]);
  } 
}

// Fade it out when we release
function mouseReleased() {
  osc.fade(0,0.5);
  //
}

