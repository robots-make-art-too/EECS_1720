# Live code from Week 4 - Feb 3

This is a cleaned up folder of our live code from lecture. 

1. JavaScript `p5.js` examples are in `/JS`
2. Python `processing.py` examples are in `/python`.

## What is in here?

We worked through:
- creating a colour gradient using _linear interpolation_
- displaying an iterative geometric pattern
- basic event-driven actions triggered by a mouse-click
- intergration of a simple _sinusoidal oscillator_

## What can I do?

1. To run any `p5.js` examples - drag the `index.html` files into a browser window
   - remember `browser`-specific methods for allowing `sound`
2. To run any `processing.py` examples - you need `processing version 3.5.4`
3. The `mouse-click` `interactions` are associated with:
   - instant `colour` and `image` refreshes
   - prolonged `sound` - if held down

---

## Uh oh it's not working

1. Did you use processing 3.5.4?
2. Did the source for `libraries` location change for p5.js examples?
   - is there somehow a library being asked for in the `index.html` file but not present in the `libraries` folder?
3. Are you trying to use an old processing file (that didn't have the `sketch.properties` file encapsulated with the `.pyde` file - inside of a same named folder?)
   - update your local repo
4. Did you try it in `Firefox`? 
   - less things to do for sound (probably just works)
5. Are you in, or did you setup, `python mode` in processing?
6. Did you import the  `sound` library in processing?
   - have to manually add it through toolbar:
     - [S]ketch > Import Library > Add Library > 'search sound' > select `sound`
7. ? ask

---

## Try these

### processing.py

What happens when you change:

1. geometric_py:
   - constantFactor? 
   - what about circleSize?
   - can you grow or shrink the shapes?
   - does it matter?
   - can you relocate the smallest shape?
2. colour_py
   - change any of the variables in lerpColor()?
     - change the 1.0 to a 1?
   - can you make the gradient flow diagonally?
   - can you make the gradient stop and start in other ways?
     - insert blank space? 
     - mutliple times using a loop?


### p5.js

Replicate the python changes in JavaScript. 
   - Are there any subtle or not so subtle differences in the output?