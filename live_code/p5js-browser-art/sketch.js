// sound
let loopBeat;
let bassSynth, cymbalSynth;
let counter;

// image
const barWidth = 20;
let lastBar = -1;

function setup() {

  // image
  createCanvas(720, 400);
  colorMode(HSB, height, height, height);
  noStroke();
  background(0);

  // sound
  counter = 0;

  bassSynth = new Tone.MembraneSynth().toDestination();
  cymbalSynth = new Tone.MetalSynth({
    "frequency": 250,
    "envelope": {
      "attack": 0.001,
      "decay": 0.1,
      "release": 0.01,
    },
    "harmonicity": 3.1,
    "modulationIndex": 16,
    "resonance": 4000,
    "octaves": 0.5,
  }).toDestination();

  loopBeat = new Tone.Loop(song, "16n");

  Tone.Transport.bpm.value = 140;
  Tone.Transport.start();
  loopBeat.start(0);
}

// sound
function song(time) {
  if (counter % 4 === 0) {
    bassSynth.triggerAttackRelease("c1", "8n", time, 1);
  }

  if (counter % 4 !== 1) {
    if (counter === 3 || counter === 12) {
        cymbalSynth.envelope.decay = 0.5;
    } else {
        cymbalSynth.envelope.decay = 0.01;
    }
    cymbalSynth.triggerAttackRelease("c1", "32n", time, 0.3);
  }
  counter = (counter + 1) % 16;
  // console.log(counter);
}

// image
function draw() {
  let whichBar = mouseX / barWidth;
  if (whichBar !== lastBar) {
    let barX = whichBar * barWidth;
    fill(mouseY, height, height);
    rect(barX, 0, barWidth, height);
    lastBar = whichBar;
  }
}
