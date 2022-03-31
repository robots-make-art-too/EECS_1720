// The midi notes of a scale
let notes = [ 60, 62, 64, 65, 67, 69, 71];

let osc;

function setup() {
  createCanvas(720, 400);
  
  // A triangle oscillator
  osc = new p5.TriOsc();
  // Start silent
  osc.start();
  osc.amp(0);
}

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
  if(event.button == 0 && event.clientX < width && event.clientY < height) {
    // Map mouse to the key index
    let key = floor(map(mouseX, 0, width, 0, notes.length));
    playNote(notes[key]);
  }
}

// Fade it out when we release
function mouseReleased() {
  osc.fade(0,0.5);
}