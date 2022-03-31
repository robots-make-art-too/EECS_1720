# About the Camera

1. _One_ camera per scene: required
2. _Unlimted_ amount of `gps-entity-place`: required for the scene, and _it_ requires `latitude` and `longitude`

---

## gps-camera

```HTML
<a-camera gps-camera rotation-reader></a-camera>
<a-box color="yellow" gps-entity-place="latitude: <your-latitude>; longitude: <your-longitude>"/>
```
Note that `rotation-reader` is super important as it lets our system actively reaad the position and/or rotation of the camera.

Some useful properties, taking only positive values, in `meters`:
- minDistance - minimum distance content will be viewed at
- maxDistance - maximum distance content can be viewed to

Other properties:
- gpsMinDistance - how far the camera (mobile) must move, in meters, to generate a `GPS` update event
- gpsTimeInterval - how often to obtain a new `GPS` position (we probably don't need this and it is set to 0 by default)

## gps-projected-camera

```HTML
<a-camera gps-projected-camera rotation-reader></a-camera>
<a-box color="yellow" gps-projected-entity-place="latitude: <your-latitude>; longitude: <your-longitude>"/>
<!-- with altitude -->
<a-box color="yellow" gps-projected-entity-place="latitude: <your-latitude>; longitude: <your-longitude>" position="0 30 0"/>
```
This value of 30 in the position parameter indicates a y-value, or altitude, of height at 30 meters displayed relative to the _camera's_ current height.

---

## Distant objects?

Are you thinking about display content far away? (1km+) 
- Maybe you want to add something to the sky?
- Maybe you want to add a spaceship hovering over the lake, way over there?

There are a few special conditions for `arjs` and must be used together:
1. sourceType: webcam; 
2. videoTexture: true;

```HTML
    <a-scene
      vr-mode-ui="enabled: false"
      embedded
      arjs="sourceType: webcam; videoTexture: true; debugUIEnabled: false;"
    >
```

## Face the camera?

Usually, in Location Based, it's nice to have `AR` content that will always face the you. This way, when you rotate the camera, 3D models, or most of all, text, they are and remain visible.

```HTML
<!-- Include this script -->
<script src="https://unpkg.com/aframe-look-at-component@0.8.0/dist/aframe-look-at-component.min.js"></script>

<!-- Then we can add the following to the a-scene -->
<a-camera gps-camera='simulateLatitude: 51.049; simulateLongitude: -0.723' rotation-reader></a-camera>

<a-text value="This will always face the user." look-at="[gps-camera]" scale="75 75 75" gps-entity-place="latitude: 51.0491; longitude: -0.723;"></a-text>
```

>
> HEY! Did you see what I did there ^^^ 
>

_We can use `simulateLatitude` and `simulateLongitude`_. There is also _`simulateAltitude`_ for setting camera altitude in meters above sea level. These are all useful for testing. We will use them.

## Camera shaking?

In location-based mode, `shaking` effects can occur due to frequent small changes in the device's orientation, due to the high sensitivity of the device sensors such as the accelerometer.

```HTML
<a-camera id='camera1' look-controls-enabled='false' arjs-look-controls='smoothingFactor: 0.1' gps-camera='gpsMinDistance: 5' rotation-reader> </a-camera>
```
Special conditions:
1. `look-controls-enabled='false'` must be disabled
2. so that `arjs-look-controls='smoothingFactor: 0.1'` can replace it

Consider also `gps-camera='gpsMinDistance: 5'` (you can change that 5, and remember it is in meters). Finally, consider that you can reduce `jumping` of augmented content when near a place - a bad-looking effect due to GPS sensors' low precision. To do so you can use the `gpsMinDistance` and `gpsTimeInterval` properties.

---

## AR `hit-test`

Want to touch something in AR? Place or position something already there? Request the `hit-test` feature.

```HTML
<a-scene webxr="optionalFeatures:  hit-test;" ar-hit-test="target:#myobject;">
	<a-entity id="myobject"></a-entity>
```

1. Properties
   - target
     - the object to move around (default null)
   - enabled
     - whether to do a hit-test or not (default true)
   - src
     - image to use for the `reticle`[1] (there is a default map saved in resources/)
   - type
     - `footprinnt` or `map` where `footprint` is the shape of the model (default "footprint")
   - footprintDepth
     - amount of model used for footprint (default 0.1, where 1 is the full height)
   - mapSize
     - size of map that is set when no target is set (default 0.5 0.5) 

2. Events
   - ar-hit-test-start
     - start scanning
   - ar-hit-test-achieved
     - found a surface to start testing against
   - ar-hit-test-select
     - when you have stopped positioning, and where the detail now contains the latest position, orientation, and inputSource 

You add it to the scene element and then when in Augmented Reality tap on the screen. Whereever you tap will be mapped to simulate where you are pointing to in the real world and place a reticle to fire events.

If you have set a target property to be an element it will automatically make the reticle to be the same size as the footprint of the target and then when the user selects the object will be teleported there. It will also set the visible state of the object to true so you can hide the object until the user has placed it for the first time. The hide-on-enter-ar component is useful for that.

You can toggle this component’s enabled state to not do any interactions until you are ready.

### Hide on enter

When included will toggle visible state

```HTML
<a-light hide-on-enter-ar></a-light>
<a-sky hide-on-enter-ar color="skyblue"></a-sky>
```

---
## Some extra things, maybe

### Oh did you want another way to serve local?

If you happen to be running a nodejs environment and have installed `npm` you can do the following (if not, don't try to install those things now, if something goes wrong, you'll be gone all weekend): 

```bash
git clone https://github.com/aframevr/aframe.git  # Clone the repository.
cd aframe && npm install  # Install dependencies.
npm start  # Start the local development server.
```
You can enable the `require` method for browsers through [browserify](https://browserify.org/#middle-section).

### Something for Saturday night

A glTF file uses one of two possible file extensions:.gltf or.glb. Both.gltf and.glb files may reference external binary and texture resources. Alternatively, both formats may be self-contained by directly embedding binary data buffers. The format was designed for compact file size, fast loading, run-time independence, and complete 3D scene representation. It is often described as "the JPEG of 3D," and can use .gltf (JSON/ASCII) or .glb (binary file format) file extensions.

[glTF workflow](https://blog.mozvr.com/a-saturday-night-gltf-workflow/)

[Which file format?](https://www.threekit.com/blog/gltf-everything-you-need-to-know)

models from [clare.io](https://clara.io/) or [Sketchfab](https://sketchfab.com/feed)

---

### Other libraries and components

- [aframe-alongpath-component](https://www.npmjs.com/package/aframe-alongpath-component)
- [aframe-lerp-component rawfile](https://unpkg.com/aframe-lerp-component@1.1.0/dist/aframe-lerp-component.min.js)
- [aframe-log-component](https://unpkg.com/aframe-log-component@1.0.7/dist/aframe-log-component.min.js)
- [aframe-particle-system](https://unpkg.com/aframe-particle-system-component@1.0.9/dist/aframe-particle-system-component.min.js)
- [aframe-text-geometry](https://www.npmjs.com/package/aframe-text-geometry-component)

---

[1]. A reticle, or reticule also known as a graticule, is a pattern of fine lines or markings built into the eyepiece of an optical device such as a telescopic sight, spotting scope, theodolite, optical microscope or the screen of an oscilloscope, to provide measurement references during visual inspections.
